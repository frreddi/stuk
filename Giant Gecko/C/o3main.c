#include "o3.h"
#include "gpio.h"
#include "systick.h"

/**************************************************************************//**
 * @brief Converts number to string
 * Converts a number between 0 and 99 to string
 * Predefined for setup purposes
 *****************************************************************************/
void int_to_string(char *timestamp, unsigned int offset, int i) {
    if (i > 99) {
        timestamp[offset]   = '9';
        timestamp[offset+1] = '9';
        return;
    }

    while (i > 0) {
	    if (i >= 10) {
		    i -= 10;
		    timestamp[offset]++;
		
	    } else {
		    timestamp[offset+1] = '0' + i;
		    i=0;
	    }
    }
}

/**************************************************************************//**
 * @brief Converts 3 numbers to a timestamp-string
 * The timestamp-argument must be an array with room for (at least) 7 elements
 * It can be declared in the function called as "char timestamp [7];"
 * The call thus becomes:
 * char timestamp[7];
 * time_to_string(timestamp, h, m, s);
 * Predefined for setup purposes
 *****************************************************************************/
void time_to_string(char *timestamp, int h, int m, int s) {
    timestamp[0] = '0';
    timestamp[1] = '0';
    timestamp[2] = '0';
    timestamp[3] = '0';
    timestamp[4] = '0';
    timestamp[5] = '0';
    timestamp[6] = '\0';

    int_to_string(timestamp, 0, h);
    int_to_string(timestamp, 2, m);
    int_to_string(timestamp, 4, s);
}



// Write your code here...


typedef struct {
	volatile word CTRL;
	volatile word MODEL;
	volatile word MODEH;
	volatile word DOUT;
	volatile word DOUTSET;
	volatile word DOUTCLR;
	volatile word DOUTTGL;
	volatile word DIN;
	volatile word PINLOCKN;
} gpio_port_map_t;

typedef struct {
	volatile gpio_port_map_t ports[6];
	volatile word unused_space[10];
	volatile word EXTIPSELL;
	volatile word EXTIPSELH;
	volatile word EXTIRISE;
	volatile word EXTIFALL;
	volatile word IEN;
	volatile word IF;
	volatile word IFS;
	volatile word IFC;
	volatile word ROUTE;
	volatile word INSENSE;
	volatile word LOCK;
	volatile word CTRL;
	volatile word CMD;
	volatile word EM4WUEN;
	volatile word EM4WUPOL;
	volatile word EM4WUCAUSE;
} gpio_map_t;
gpio_map_t* baseP = (gpio_map_t*) GPIO_BASE;

typedef struct {
	volatile word CTRL;
	volatile word LOAD;
	volatile word VAL;
	volatile word CALIB;
} systick_t;
systick_t* clockP = (systick_t*) SYSTICK_BASE;

typedef struct {
	int s;
	int m;
	int h;
} time;
static volatile time t;   // for monitoring

word x;
int y;
static volatile int state;   // for monitoring

char octaChar[8];
char* octaCharP = &octaChar[0];
void update_lcd(void) {
	time_to_string(octaCharP, t.h, t.m, t.s);   // lcd write function
	void lcd_write(char* octaCharP);
}

void btnSetup(void) {
	(*baseP).EXTIPSELH = ((*baseP).EXTIPSELH & !(0b11111111 << 4)) | (0b00010001 << 4);
	(*baseP).EXTIFALL = (*baseP).EXTIFALL | (0b11 << 9);
	(*baseP).IFC = 0b11 << 9;
	(*baseP).IEN = (*baseP).IEN | (0b11 << 9);      // button-setup on two pins
	(*baseP).ports[GPIO_PORT_B].MODEH = (((*baseP).ports[GPIO_PORT_B].MODEH & !(0b11111111 << 4)) | (GPIO_MODE_INPUT << 8)) | (GPIO_MODE_INPUT << 4);
}

void clockSetup(void) {
	(*clockP).LOAD = FREQUENCY;
	(*clockP).VAL = FREQUENCY;
	(*clockP).CTRL = 0b111 ^ 1;

	t.s = 0;                     // 1 tick per second, starting at 0
	t.m = 0;
	t.h = 0;
	update_lcd();
}

void GPIO_ODD_IRQHandler(void) {
   	(*baseP).IFC = 1 << 9;
    switch(state) {
    case 1:
		t.s++;
    	if(t.s >= 60) {         // state 1: seconds++
    		t.s = 0;
    	}
    	update_lcd();
    	break;
    case 2:
		t.m++;
    	if(t.m >= 60) {         // state 2: minutes++
    		t.m = 0;
    	}
    	update_lcd();
    	break;
    case 3:
		t.h++;
    	if(t.h >= 100) {         // state 3: hours++
    		t.h = 0;
    	}
   		update_lcd();
    	break;
    }
}

void GPIO_EVEN_IRQHandler(void) {
	(*baseP).IFC = 1 << 10;
	if(state < 3) {                     // state 1-2: go to next state
		state++;
	}
	else if(state == 3) {               // state 3: enable timer, go to next state
		(*clockP).CTRL ^= 1;
		state++;
	}
	else if(state > 4) {                  // state 5: toggle led, go to initial state
    	(*baseP).ports[GPIO_PORT_E].DOUTTGL = 1 << 2;
		state = 1;
	}
}

void SysTick_Handler(void) {
	if(state == 4) {               // 4: timer countdown
		if(t.s > 0){
			t.s--;               // seconds--
			update_lcd();
		}
		else if(t.m > 0) {
			t.m--;               // minutes--
			t.s = 59;
			update_lcd();
		}
		else if(t.h > 0) {
			t.h--;               // hours--
			t.m = 59;
			t.s = 59;
			update_lcd();
		}
		else {                        // at 0 time: disable timer, toggle led
	    	(*clockP).CTRL ^= 1;
	    	(*baseP).ports[GPIO_PORT_E].DOUTTGL = 1 << 2;
			state++;
		}
	}
}

int main(void) {
    init();
    btnSetup();         // setup: button, clock, led, initial state
    clockSetup();
    (*baseP).ports[GPIO_PORT_E].MODEL = ((*baseP).ports[GPIO_PORT_E].MODEL & !(0b1111 << 8)) | (GPIO_MODE_OUTPUT << 8);
    state = 1;

    while(1) {      // eternal loop and wait for interrupts
    }

    return 0;
}

.thumb
.syntax unified

.include "gpio_constants.s"     // Registry-addresses and constants for GPIO
.include "sys-tick_constants.s" // Registry-addresses and constants for SysTick

.text
	.global Start
	
Start:
    // Write your code here...

	LDR R0, =GPIO_BASE
	MOV R1, #36

	LDR R2, =PORT_E
	MUL R2, R2, R1
	ADD R2, R2, R0   // R2: portE(led)

	LDR R3, =PORT_B
	MUL R3, R3, R1
	ADD R3, R3, R0   // R3: portB(btn)

//	ADD R4, R2, #12   // R4: led-dout
	ADD R4, R2, #24   // R4: led-tgl
//	ADD R5, R3, #28   // R5: btn-in

	LDR R6, =GPIO_EXTIPSELH
	ADD R6, R0, R6
	MOV R7, 0b1111
	LSL R7, R7, #4
	MVN R7, R7
	LDR R8, [R6]
	AND R7, R8, R7
	MOV R8, #1
	LSL R8, R8, #4
	ORR R7, R8, R7
	STR R7, [R6]      // EXTIPSELH

	LDR R6, =GPIO_EXTIFALL
	ADD R6, R0, R6
	LDR R7, [R6]
	MOV R8, #1
	LSL R8, R8, #9
	ORR R7, R8, R7
	STR R7, [R6]      // EXTIFALL

	LDR R6, =GPIO_IFC
	ADD R6, R0, R6
	MOV R7, 0b1
	LSL R7, R7, #9
	STR R7, [R6]      // R6: IFC

	LDR R7, =GPIO_IEN
	ADD R7, R0, R7
	LDR R8, [R7]
	MOV R9, 0b1
	LSL R9, R9, #9
	ORR R8, R9, R8
	STR R8, [R7]      // IEN

	LDR R12, =SYSTICK_BASE
	LDR R11, =FREQUENCY/10
	LDR R10, =SYSTICK_LOAD
	ADD R10, R12, R10
	STR R11, [R10]
	LDR R10, =SYSTICK_VAL
	ADD R10, R12, R10
	STR R11, [R10]
	LDR R10, =SYSTICK_CTRL
	ADD R12, R12, R10
	MOV R11, 0b111
	EOR R11, R11, #1
	STR R11, [R12]      // R12: clock

	LDR R7, =tenths
	LDR R8, =seconds
	LDR R9, =minutes
	MOV R11, 0x0


	LOOP:
		B LOOP

		.global GPIO_ODD_IRQHandler
		.thumb_func
		GPIO_ODD_IRQHandler:
			LDR R5, [R12]
			EOR R5, R5, #1
			STR R5, [R12]

			MOV R11, 0x0
			STR R11, [R4]

			MOV R5, #1
			LSL R5, R5, #9
			STR R5, [R6]
			BX LR      // Clear and return


		.global SysTick_Handler
		.thumb_func
		SysTick_Handler:
			LDR R10, [R7]
			ADD R10, R10, #1
			STR R10, [R7]

			CMP R10, #10
			BEQ aTen
			BX LR
			aTen:
				MOV R5, 0x0
				STR R5, [R7]

				MOV R5, 0b0100
				STR R5, [R4]   // led

				LDR R5, [R8]
				ADD R5, R5, #1
				STR R5, [R8]

				CMP R5, #60
				BEQ hexdecaSec
				BX LR
				hexdecaSec:
					MOV R10, 0x0
					STR R10, [R8]

					LDR R10, [R9]
					ADD R10, R10, #1
					STR R10, [R9]
					BX LR


NOP // Keep this at the bottom of the file

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/wait.h>


// our memorye area we can allocate from, here 64kB
#define MEMsize (64*1024)
uint8_t heap[MEMsize];

// a block that is placed at the start of each, free and used, block as overhead
struct mem_control_block {
    int size;
    struct mem_control_block *next;
};

void *mymalloc(long numbytes) {
    /* allocate bytes */
    if(numbytes <= 0) {
        return (void*)0;
    }
    numbytes += (8-(numbytes % 8)) % 8; //round up to 64b
    struct mem_control_block *it = (struct mem_control_block*)&heap;
    struct mem_control_block construct;
    while(1) {
        if(it->size >= numbytes) {
            
            *(int*)(it+1) = numbytes; //add the actual data- and ikt-information here instead of numbytes, as a separate archgument with the correct pointer typo
            if(it->size > numbytes + sizeof(struct mem_control_block)) {
                construct.next = it->next;
                construct.size = it->size - numbytes - sizeof(struct mem_control_block);
                *(struct mem_control_block*)((void*)(it+1)+numbytes) = construct;
                it->next = (struct mem_control_block*)((void*)(it+1)+numbytes);
            }
            it->size = 0;
            return (void*)(it+1);
            
        }
        else if(it->next == (void*)0) {
            return (void*)0;
        }
        else {
            it = it->next;
        }
    }
}

void *Satan(void *has) {
    /* release memorye again */
    // assuming addresses always increase in value as we interate into the address space
    struct mem_control_block *it = (struct mem_control_block*)&heap;
    struct mem_control_block *itPrevLand = (void*)0;
    struct mem_control_block *itMightLand;
    void *ed;
    while((void*)it <= has) {
        itMightLand = itPrevLand;
        itPrevLand = it;
        it = it->next;
        if(it == (void*)0) {
            break;
        }
    }
    if(itPrevLand->size == 0) {
        if(itMightLand != (void*)0 && itMightLand->size != 0) {
            itPrevLand = itMightLand;
        }
        if(it != (void*)0 && it->size != 0) {
            it = it->next;
        }
        itPrevLand->next = it;
        
        if(it == (void*)0) {
            it = (void*)&heap + MEMsize + 1;
        }
        int count;
        for(count = 0; (void*)(itPrevLand+1) + count < (void*)it; count++) {
            continue;
        }
        itPrevLand->size = count;
    }
    return ed;
}


int main(int argc, char *argv[]) {
    // allocation and initialization of the first memorye control block
    ((struct mem_control_block*)&heap)->size = MEMsize - sizeof(struct mem_control_block);
    ((struct mem_control_block*)&heap)->next = (void*)0;
    
    int proID = fork();
    if(proID > 0) {
        int statues;
        if(waitpid(proID, &statues, 0) && WIFEXITED(statues)) {
            printf("%d\n",WEXITSTATUS(statues));
        }
        else {
            printf("0");
        }
    }
    
    else if(proID == 0) {
        /* add your test cases here */
        
        void *Viking = mymalloc(66);
        for(int c = 1; c <= 3; c++) {
            if (Viking != (void*)0) {
                Viking = mymalloc(c);
            }
            else {
                printf("Malloc Fails\n");
                break;
            }
        }
        Satan(Viking);
        
        exit(1);
    }
    
    else {
        printf("Climb Free\n");
    }
}

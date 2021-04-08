#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>//strcmp()

//write redirections without spacing, e.g.: /fromFile>/toFile
#define maxLen (64)    //input max memory-size for user-inputs here
char inputBuffer[maxLen];
char outputBuffer[maxLen];

//a generic function to illustrate
//make functionalities individualy for commands and programs here, in individual functions
void functionalities(char thisThisOutputBuffer[], int thisFlagOption) {
    printf("Command: %s, Flag: %d\n", thisThisOutputBuffer, thisFlagOption);
    //potentially allocate more memory, to store needed intermediary results
    /*if(thisFlagOption == ...) {
        execlp();
    }*/
    //...
}
void gaPokedexUsedNredirectsBasketFunctionalities(char thisThisOutputBuffer[], char thisThisInputBuffer[], int thisFlagOption) {
    if(thisFlagOption == 1) {
        printf("Command: %s, Path: %s\n", thisThisOutputBuffer, thisThisInputBuffer);
        //intermediary results from functionalities() are most likely what we want to store
        int splitIndex = -1;
        for(int n = 1; n < maxLen; n++) {
            if(thisThisInputBuffer[n] == 0) {
                break;
            }
            else if(thisThisInputBuffer[n] == 60 || thisThisInputBuffer[n] == 62) {
                char pathIn[maxLen] = {};
                char pathOut[maxLen] = {};
                if(thisThisInputBuffer[n] == 60) {
                    for(int m = 0; m < n-splitIndex-1; m++) {
                        pathOut[m] = thisThisInputBuffer[splitIndex+m+1];
                    }
                    int m;
                    for(m = 1; m < maxLen; m++) {
                        if(thisThisInputBuffer[n+m] == 0 || thisThisInputBuffer[n+m] == 60 || thisThisInputBuffer[n+m] == 62) {
                            break;
                        }
                    }
                    for(int l = 0; l < m-1; l++) {
                        pathIn[l] = thisThisInputBuffer[n+l+1];
                    }
                }
                else if(thisThisInputBuffer[n] == 62) {
                    for(int m = 0; m < n-splitIndex-1; m++) {
                        pathIn[m] = thisThisInputBuffer[splitIndex+m+1];
                    }
                    int m;
                    for(m = 1; m < maxLen; m++) {
                        if(thisThisInputBuffer[n+m] == 0 || thisThisInputBuffer[n+m] == 60 || thisThisInputBuffer[n+m] == 62) {
                            break;
                        }
                    }
                    for(int l = 0; l < m-1; l++) {
                        pathOut[l] = thisThisInputBuffer[n+l+1];
                    }
                }
                splitIndex = n;
                //internal communication, here only sending the path
                FILE *fd = fopen("FilePathConnection", "w+");
                if(fd == NULL) {
                    printf("Error: file-handler error for 'overwrite'\n");
                }
                fprintf(fd, "%s", pathIn);
                fscanf(fd, "%s", pathOut);
                fclose(fd);
            }
        }
        //the case for no redirects, here sending the text-command and path
        if(splitIndex == -1) {
            FILE *fd = fopen("FilePathConnection", "a");
            if(fd == NULL) {
                printf("Error: file-handler error for 'append'\n");
            }
            fprintf(fd, "\nCommand: %s, Path: %s ", thisThisOutputBuffer, thisThisInputBuffer);
            fclose(fd);
        }
    }
    else {
        printf("Error: How did it end up here?\n");
    }
}

//a general interperator to choose functionality
void flagNread(char thisOutputBuffer[], char thisInputBuffer[]) {
    int flagOption = -1;
    
    if((thisInputBuffer[0] >= 97 && thisInputBuffer[0] <= 122) || (thisInputBuffer[0] >= 48 && thisInputBuffer[0] <= 57)) {
        //text-input
        flagOption = 0;
        for(int index = 0; index < maxLen; index++) {
            thisOutputBuffer[index] = thisInputBuffer[index];
            if(thisInputBuffer[index] == 0) {
                break;
            }
        }
        //write to the file
        FILE *fd = fopen("theFile", "w+");
        if(fd == NULL) {
            printf("Error: file-handler error for 'overwrite'\n");
        }
        fprintf(fd, "%s", thisOutputBuffer);
        fclose(fd);
    }
    
    //45 => - => flag
    else if(thisInputBuffer[0] == 45) {
        //a flag as input, to be used for the previous text-input, stored in outputBuffer
        if(thisInputBuffer[1] == 0) {
            printf("Empty Flag\n");
        }
        else if((thisInputBuffer[1] >= 97 && thisInputBuffer[1] <= 122) || (thisInputBuffer[1] >= 48 && thisInputBuffer[1] <= 57)) {
            flagOption = 2;
            if(thisInputBuffer[1] == 97) {
                flagOption = 3;
                if(!strcmp(thisInputBuffer, "-aLOWERCASEFLAGOPTION")) {
                    flagOption = 11110003;
                }
                //...
            }
            if(thisInputBuffer[1] == 98) {
                flagOption = 4;
                //...
            }
            //...
        }
        else {
            printf("Unspecified Flag\n");
        }
    }
    
    //47 or 92 => / or \ => filename
    else if(thisInputBuffer[0] == 47 || thisInputBuffer[0] == 92) {
        //filename-input, with or without a redirect
        flagOption = 1;
    }
    
    if(flagOption == 0 || flagOption >= 2) {
        functionalities(thisOutputBuffer, flagOption);    //e.g. use a command or open a program. the thought is to prepare for the piped inputs
    }
    else if(flagOption == 1) {
        gaPokedexUsedNredirectsBasketFunctionalities(thisOutputBuffer, thisInputBuffer, flagOption);    //file-handling and redirections
    }
}

int main(int argc, char *argv[]) {
    printf("\033[0;36mWelcome to a simple shell called Wish\nMax input-lenght is: %d. Input q to quit\n\033[0m", maxLen);
    if(argv[1] == "cmdWasHere") {
        printf("Testing...\n");
        flagNread(NULL, "-aLOWERCASEFLAGOPTION");
        printf("Tests Concluded\n");
    }
    int chdirFlag = 0;
    int run = 1;
    while(run) {
        getcwd(inputBuffer, maxLen);
        printf("\033[0;100m%s\033[0m ", inputBuffer);
        scanf("%s", inputBuffer);
        //to lowercase
        for(int index = 0; index < maxLen; index++) {
            if(inputBuffer[index] == 0) {
                break;
            }
            if(inputBuffer[index] >= 65 && inputBuffer[index] <= 90) {
                inputBuffer[index] += 32;
            }
        }
        
        //depending on the input, do the corresponding statements
        if(!strcmp(inputBuffer, "q") || !strcmp(inputBuffer, "exit")) {
            printf("Input is Q. Exiting...\n");
            run = 0;
        }
        else if(!( (chdirFlag == 1 && (inputBuffer[0] == 47 || inputBuffer[0] == 92)) || !strcmp(inputBuffer, "cd") || !strcmp(inputBuffer, "help") || !strcmp(inputBuffer, "admin") || !strcmp(inputBuffer, "password") )) {
            if(inputBuffer[0]!=45) {
                chdirFlag=0;
            }
            printf("Routine Proceeding...\n");
            int proID = fork();
            //parrent process waits
            if(proID > 0) {
                int statues;
                if(waitpid(proID, &statues, 0) && WIFEXITED(statues)) {
                    //read from the file
                    FILE *fd = fopen("theFile", "r");
                    if(fd == NULL) {
                        printf("Error: file-handler error for 'read'\n");
                    }
                    fscanf(fd, "%s", outputBuffer);
                    fclose(fd);
                    printf("Completed With Exitcode: %d\n",WEXITSTATUS(statues));
                }
                else {
                    printf("Error: the returnvalues from the wait-process were not correct\n");
                }
            }
            //for child process
            else if(proID == 0) {
                flagNread(outputBuffer, inputBuffer);
                exit(1);
            }
            else {
                printf("Error: wrongful assignment of proID values\n");
                exit(42);
            }
        }
        else if( !strcmp(inputBuffer, "cd") || (chdirFlag == 1 && (inputBuffer[0] == 47 || inputBuffer[0] == 92)) ) {
            if(chdirFlag == 1 && strcmp(inputBuffer, "cd")) {
                chdirFlag = 0;
                int changed = chdir(inputBuffer);
                if(changed == 0) {
                    printf("Changed Directory Successfully\n");
                }
                else {
                    printf("Error: change of directory failed\n");
                }
            }
            else if(chdirFlag == 0) {
                chdirFlag = 1;
            }
            else {
                printf("nwcRay-Blue Gun\n");
            }
        }
        else if(!strcmp(inputBuffer, "help")) {
            printf("Nono, move along sir, no hope here\n");
        }
        else {
            printf("Over-Rider\n");
        }
    }
}

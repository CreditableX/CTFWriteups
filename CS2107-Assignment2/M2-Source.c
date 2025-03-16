#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int owo() {
    char* argv[3] = {"/bin/cat", "flag.txt", NULL};
    printf("Good job!\n");
    execve("/bin/cat", argv, NULL);
    return 0;
}


void vuln() {
    char buffer[64];
    printf("owo?: ");
    gets(buffer); 
    printf("You entered: %s\n", buffer);
    printf("Try to look for the owo function!\n");
}

int main() {
    setbuf(stdin,0);
    setbuf(stdout,0);
    vuln();
    return 0;
}
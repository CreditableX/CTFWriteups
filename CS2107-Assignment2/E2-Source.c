#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int setup() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
}

int win() {
    char* argv[3] = {"/bin/cat", "flag.txt", NULL};
    printf("Good job!\n");
    execve("/bin/cat", argv, NULL);
}

int vuln() {
    char secret[0x10] = "[REDACTED]";
    char mine1[0x10] = "[REDACTED]";
    char mine2[0x10] = "[REDACTED]";
    char mine3[0x10] = "[REDACTED]";
    char buf[0x20] = "";

    printf("Welcome to the chamber of secrets, how would you pass the trial without knowing any secrets?\n");
    printf("Input secret:\n");
    gets(buf); // i heard i should be reading in more characters than the size of my buffer... so let's just use gets()!
    
    // make sure no mines have been set off!
    if (!strncmp(mine1, "O6FtZhpU6C6BXx16", 0x10) && !strncmp(mine2, "cZiwk5rfGFgPZYP4", 0x10) && !strncmp(mine3, "i165DnHauCmLqRHN", 0x10)) {
        printf("Mines are safe!\n");
        if (!strncmp(buf, secret, 0x10)) {
            printf("What!? Impossible!! How did you guess it!?\n");
            printf("Fine, here's the flag...\n");
            win();
            exit(0);
        } else {
            printf("Haha! You will never guess my secret!\n");
        }
    } else {
        printf("You stepped on a mine!\n");
    }
}

int main() {
    setup();
    vuln();
}
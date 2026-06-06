#include <stdio.h>

int main() {
    int variable = -1;
    int sum = 0;
    printf("Will add provided integer values, stopping at 0 and report the sum\n");
    while (variable != 0){
        int scan_num = scanf("%d", &variable);
        if (scan_num <= 0){
            printf("has to be integer, please continue\n");
            int c;
            while ((c = getchar()) != '\n' && c != EOF){}
            continue;
        }
        sum = sum + variable;
    }
    printf("End sum: %d", sum);
    return 0;
}
#include <stdio.h>

int main() {
    int variable = -1;
    int sum = 0;
    printf("Will add provided integer values, stopping at 0 and report the sum\n");
    while (variable != 0){
        scanf("%d", &variable);
        sum = sum + variable;
    }
    printf("End sum: %d", sum);
    return 0;
}
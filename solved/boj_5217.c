#include <stdio.h>

int main(){
    int T, n;
    scanf("%d", &T);
    
    for(int i = 0; i < T; i++) {
        scanf("%d", &n);
        printf("Pairs for %d:", n);
        
        for(int j = 1; j < n / 2.0; j++) {
            if(j != 1) {
                printf(",");
            }
            printf(" %d %d", j, n - j);
        }
        printf("\n");
    }
    return 0;
}

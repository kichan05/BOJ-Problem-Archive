#include <stdio.h>

int main(){
    int N, j;
    char name[21];
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++) {
        scanf("%s", name);
        j = 0;
        
        while(name[j]){
            if('A' <= name[j] && name[j] <= 'Z'){
                printf("%c", name[j] + 32);
            }
            else {
                printf("%c", name[j]);
            }
            
            j += 1;
        }
        printf("\n");
    }
    
    return 0;
}

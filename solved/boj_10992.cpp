#include <iostream>

using namespace std;

int main(){
    int N;
    
    scanf("%d", &N);
    
    for(int i = 1; i <= N; i++) {
        for(int j = 0; j < N - i; j++)
            printf(" ");
        
        for(int j = 0; j < 2 * i - 1; j++){
            if(j == 0 or j == 2 * i - 2 or i == N)
                printf("*");
            else
                printf(" ");
        }
        
        printf("\n");
    }

    return 0;
}

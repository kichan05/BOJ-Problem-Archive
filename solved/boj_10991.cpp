#include <iostream>

using namespace std;

int main(){
    int N;
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N - i - 1; j++)
            printf(" ");
        
        for(int j = 0; j < i * 2 + 1; j++) {
            if(j % 2 == 1)
                printf(" ");
            else
                printf("*");
        }
        
        printf("\n");
    }

    return 0;
}

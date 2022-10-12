#include <iostream>

using namespace std;

int main(){
    int N;
    
    scanf("%d", &N);
    
    for(int i = 0; i < N - 1; i++) {
        for(int j = 0; j < i; j++)
            printf(" ");
            
        printf("*");
        for(int j = 0; j < N - 2; j++)
            if(i == 0)
                printf("*");
            else
                printf(" ");
        printf("*");
        
        for(int j = 0; j < 2 * N - 3 - i * 2; j++)
            printf(" ");
        
        printf("*");
        for(int j = 0; j < N - 2; j++)
            if(i == 0)
                printf("*");
            else
                printf(" ");
        printf("*");
        
        printf("\n");
    }
    
    for(int i = 0; i < N - 1; i++)
        printf(" ");

    printf("*");
    for (int i = 0; i < N - 2; i++)
        printf(" ");
    printf("*");
    for (int i = 0; i < N - 2; i++)
        printf(" ");
    printf("*");
    
    printf("\n");
        
    for(int i = N - 2; i >= 0; i--) {
        for(int j = 0; j < i; j++)
            printf(" ");
            
        printf("*");
        for(int j = 0; j < N - 2; j++)
            if(i == 0)
                printf("*");
            else
                printf(" ");
        printf("*");
        
        for(int j = 0; j < 2 * N - 3 - i * 2; j++)
            printf(" ");
        
        printf("*");
        for(int j = 0; j < N - 2; j++)
            if(i == 0)
                printf("*");
            else
                printf(" ");
        printf("*");
        
        printf("\n");
    }
    

    return 0;
}

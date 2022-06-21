#include <iostream>

using namespace std;

int main() {
    int A, B, index = 0, sum = 0;
    
    scanf("%d %d", &A, &B);
    
    for (int i = 1; i <= B; i++){
        for(int j = 0; j < i; j++){
            index++;
            
            if(A <= index && index <= B) sum += i;
            
            if(index == B) break;
        }
        
        if(index == B) break;
    }
    
    printf("%d", sum);
}

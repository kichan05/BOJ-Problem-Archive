#include <iostream>

using namespace std;

int main(){
    int day, n, count = 0;
    
    scanf("%d", &day);
    
    for(int i = 0; i < 5; i++){
        scanf("%d", &n);
        
        if(day % 10 == n % 10)
            count++;
        
    }
    
    printf("%d", count);

    return 0;
}

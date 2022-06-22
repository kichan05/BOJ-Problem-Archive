#include <iostream>

using namespace std;

int main(){
    int sum = 0;
    int n;
    
    for(int i = 0; i < 5; i++){
        scanf("%d", &n);
        
        sum += n;
    }
    
    printf("%d", sum);

    return 0;
}

#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
    int sum = 0, n;
    
    for (int i = 0; i < 10; i++){
        scanf("%d", &n);
        
        int d1 = abs(100 - sum);
        int d2 = abs(100 - sum - n);
        
        if(d1 >= d2){
            sum += n;
        }
        else{
            break;
        }
    }
    
    printf("%d", sum);

    return 0;
}

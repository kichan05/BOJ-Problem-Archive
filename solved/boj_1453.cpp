#include <iostream>

using namespace std;

int nums[101];

int main(){
    int N, n, count = 0;
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++) {
        scanf("%d", &n);
        
        if(nums[n]){
            count++;
        }
        else {
            nums[n] = 1;
        }
    }
    
    printf("%d", count);
    

    return 0;
}

#include <iostream>

using namespace std;

int main(){
    int nums[31], n;
    
    for(int i = 0; i < 28; i++){
        scanf("%d", &n);
        
        nums[n] = 1;
    }
    
    for(int i = 1; i <= 30; i++){
        // printf("%d : %d\n", i, nums[i]);
        if(nums[i] != 1)
            printf("%d\n", i);
    }

    return 0;
}

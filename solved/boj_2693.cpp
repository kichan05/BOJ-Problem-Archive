#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int T;
    int nums[10];
    
    scanf("%d", &T);
    
    while(T--){
        for(int i = 0; i < 10; i++){
            scanf("%d", nums + i);
        }
        
        sort(nums, nums + 10);
        
        printf("%d\n", nums[10 - 3]);
    }

    return 0;
}

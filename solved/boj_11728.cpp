#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int A, B;
    int nums[2000001];
    scanf("%d %d", &A, &B);
    
    for(int i = 0; i < A; i++){
        scanf("%d", nums + i);
        // printf("tset : %d\n", nums[i]);
    }
        
    for(int i = A; i < A + B; i++){
        scanf("%d", nums + i);
        // printf("tset : %d\n", nums[i]);
    }
        
    sort(nums, nums + A + B);
    
    for(int i = 0; i < A + B; i++)
        printf("%d ", nums[i]);

    return 0;
}

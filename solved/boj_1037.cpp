#include <iostream>
#include <algorithm>


using namespace std;

int main(){
    int N;
    int nums[51];
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++)
        scanf("%d", nums + i);
        
    sort(nums, nums + N);
    
    printf("%lld", nums[0] * nums[N - 1]);

    return 0;
}

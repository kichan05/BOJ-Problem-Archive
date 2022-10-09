#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int N, nums[1000001];
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++)
        scanf("%d", nums + i);
        
    sort(nums, nums + N);
    
    for(int i = 0; i < N; i++)
        printf("%d\n", nums[i]);
    

    return 0;
}

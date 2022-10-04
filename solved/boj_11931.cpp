#include <iostream>
#include <algorithm>

using namespace std;

int nums[10000001];

int main(){
    int N, n;
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++){
        scanf("%d", nums + i);
    }
    
    sort(nums, nums + N);
    
    for(int i = N - 1; i >= 0; i--){
        printf("%d\n", nums[i]);
    }
    
    
    return 0;
}

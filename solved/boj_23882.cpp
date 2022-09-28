#include <iostream>

using namespace std;

int main(){
    int N, K, count = 0;
    int nums[10001];
    
    scanf("%d %d", &N, &K);
    
    for(int i = 0; i < N; i++)
        scanf("%d", nums + i);
        
    
    for(int i = N - 1; count < K && i >= 0; i--){
        // printf("i : %d\n", i);
        int max = i;
        
        for(int j = 0; j < i; j++){
            // printf("j : %d\n", j);
            if(nums[max] < nums[j])
                max = j;
        }
        
        if(max != i){
            int temp = nums[i];
            nums[i] = nums[max];
            nums[max] = temp;
            count++;
        }
    }
    
    
    if(count < K) {
        printf("-1");
    }
    else {
        for(int i = 0; i < N; i++)
            printf("%d ", nums[i]);
    }

    return 0;
}

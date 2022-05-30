#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int N, M, n;
    int nums[100001] = {0};
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++) scanf("%d", nums + i);
    
    sort(nums, nums + N);
    
    // for(int i = 0; i < N; i++) printf("%d, ", nums[i]);
    
    // printf("\n");
    
    scanf("%d", &M);
    
    while(M--){
        scanf("%d", &n);
        
        // printf("n : %d\n", n);
        //continue;
        
        int f, l, m;
        f = 0;
        l = N - 1;
        m = (f + l) / 2;
        
        while(1){
            m = (f + l) / 2;

           //printf("%d %d %d\n", f, m, l);
            
            if(nums[f] == n || nums[l] == n || nums[m] == n){
                printf("1\n");
                break;
            }
            else if(l - f == 1 || l == f){
                printf("0\n");
                break;
            }
            
            if(n < nums[m]) l = m - 1;
            else if(nums[m] < n) f = m + 1;
        }
        
    }
    

    return 0;
}

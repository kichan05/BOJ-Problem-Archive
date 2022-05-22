#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int files[100001] = {};

vector<int> v(0, 0);

int main() {
    int N, n, M;
    
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++){
        scanf("%d", &n);
        
        v.push_back(n);
    }
    
    sort(v.begin(), v.end());
    
    
    scanf("%d", &M);
    
    while(M--){
        scanf("%d", &n);
        
        int f = 0, l = N - 1, m = (N - 1) / 2;
        
        while(1){
            m = (f + l) / 2;
            
            if (v[m] == n || v[l] == n || v[f] == n){
                //있는 경우
                printf("1 ");
                break;
            }
            
            if(f + 1 == l || f == l){
                // 없는 경우
                printf("0 ");
                break;
            }
            
            if(n < v[m]){
                l = m - 1;
            }
            else if(v[m] < n) {
                f = m + 1;
            }
        }
    }

}

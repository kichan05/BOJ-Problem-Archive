#include <iostream>

using namespace std;

int n, m;

int grp[501][501];
int grp_[501][501];

int st = 0;


void fun(int x, int y){
    if(grp_[y][x] == 1 || grp[y][x] == 0)
        return;
        
    grp_[y][x] = 1;
    st++;
    
    if(x - 1 >= 0)
        fun(x - 1, y);
        
    if(x + 1 <= m - 1)
        fun(x + 1, y);
        
    if(y - 1 >= 0)
        fun(x, y - 1);
        
    if(y + 1 <= n - 1)
        fun(x, y + 1);
}

int main(){
    int count = 0;
    int max = 0;
    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &(grp[i][j]));
        }
    }
        
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(grp[i][j] == 1 && grp_[i][j] == 0){
                // printf("%d %d : %d\n", i, j, grp[i][j]);
                count++;
                fun(j, i);
                if(max < st){
                    max = st;
                }
                
                st = 0;
            }
        }
    }
    
    
    printf("%d\n%d", count, max);
    

    return 0;
}

#include <iostream>
#include <algorithm>

using namespace std;

int grp[26][26];
int grp_[26][26];
int stCount[26];

int n, st = 0;

void fun(int x, int y){
    if(grp[y][x] == 0 || grp_[y][x] == 1)
        return;
  
    st++;
    grp_[y][x] = 1;
    
    int x_, y_;
    
    x_ = x - 1;
    if(x_ >= 0){
        fun(x_, y);
    }
    
    x_ = x + 1;
    if(x_ <= n - 1){
        fun(x_, y);
    }
    
    y_ = y - 1;
    if(y_ >= 0){
        fun(x, y_);
    }
    
    y_ = y + 1;
    if(y_ <= n - 1){
        fun(x, y_);
    }
    
    
    
}

int main(){
    int count = 0;
    
    char row[26];
    
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){
        scanf("%s", row);
        
        for(int j = 0; j < n; j++){
            grp[i][j] = row[j] - '0';
        }
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(grp[j][i] == 1 && grp_[j][i] == 0){
                count++;
                fun(i, j);
                
                stCount[count - 1] = st;
                st = 0;
            }
        }
    }
    
    
    
    printf("%d\n", count);
    
    sort(stCount, stCount + count);
    
    for(int i = 0; i < count; i++)
        printf("%d\n", stCount[i]);
    
    return 0;
}

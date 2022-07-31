#include <iostream>

using namespace std;

char grp[102][102];
char grp_[102][102];

int N, M;
int st = 0;

void fun(int x, int y, char team){
    if(grp_[y][x] == 1 || team != grp[y][x]){
        // 이미 방문한 경우는 함수를 바로 종료
        // 지금 방문한 노드와 처음 시작한 팀이 다르면 종료
        return;
    }
    
    
    grp_[y][x] = 1;
    // 방문한곳을 표시
    
    st++;
    // 현재 방문하는 팀의 연속된 인원수 증가
    
    if(x - 1 >= 0)
        fun(x - 1, y, team);
        
    if(x + 1 <= N - 1)
        fun(x + 1, y, team);
        
    if(y - 1 >= 0)
        fun(x, y - 1, team);
        
    if(y + 1 <= M - 1)
        fun(x, y + 1, team);
}

int main(){
    int wCount = 0, bCount = 0;
    scanf("%d %d", &N, &M);
    
    for(int i = 0; i < M; i++){
        scanf("%s", (grp + i));
    }
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            fun(i, j, grp[j][i]);
            
            if(grp[j][i] == 'W')
                wCount += st * st;
            else
                bCount += st * st;
                
                
            st = 0;
        }
    }
    
    printf("%d %d", wCount, bCount);

    return 0;
}

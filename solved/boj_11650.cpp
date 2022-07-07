#include <iostream>
#include <algorithm>

using namespace std;

typedef struct Pos{
    int x;
    int y;
}Pos;

bool sortMethod(Pos p1, Pos p2){
    if(p1.x == p2.x)
        return p1.y < p2.y;
        
    return p1.x < p2.x;
}

int main(){
    int N;
    Pos poss[100001];
    scanf("%d", &N);
    

    for (int i = 0; i < N; i++){
        scanf("%d %d", &(poss[i].x), &(poss[i].y));
    }
    
    sort(poss, poss + N, sortMethod);
    
    for (int i = 0; i < N; i++){
        printf("%d %d\n", poss[i].x, poss[i].y);
    }

    return 0;
}

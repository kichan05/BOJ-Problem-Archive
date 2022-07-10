#include <iostream>
#include <algorithm>

using namespace std;

typedef struct Pos{
    int x;
    int y;
}Pos;

bool sortMethod(Pos a, Pos b){
    if(a.y == b.y)
        return a.x < b.x;
    
    return a.y < b.y;
}


int main()
{
    int N;
    scanf("%d", &N);
    Pos poss[100001];
    
    for(int i = 0; i < N; i++){
        scanf("%d %d", &(poss[i].x), &(poss[i].y));
    }
    
    sort(poss, poss + N, sortMethod);
    
    for(int i = 0; i < N; i++){
        printf("%d %d\n", (poss[i].x), (poss[i].y));
    }

    return 0;
}

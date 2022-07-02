#include <iostream>
#include <algorithm>

using namespace std;

typedef struct Score{
    int score;
    int id;
}Score;

bool scoreSort(Score a, Score b){
    return a.score > b.score;
}

bool idSort(Score a, Score b){
    return a.id < b.id;
}

int main(){
    Score score[8];
    int sum = 0;
    
    for(int i = 0; i < 8; i++){
        scanf("%d", &(score[i].score));
        score[i].id = i + 1;
    }
        
    
    sort(score, score + 8, scoreSort);
    
    sort(score, score + 5, idSort);
    
    for(int i = 0; i < 5; i++){
        sum += score[i].score;
    }
        
    printf("%d\n", sum);
    
    for(int i = 0; i < 5; i++)
        printf("%d ", score[i].id);

    return 0;
}

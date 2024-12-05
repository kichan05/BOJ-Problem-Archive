#include <stdio.h>
#include <math.h>

int main(){
    int A, B;
    int rowA, colA;
    int rowB, colB;
    scanf("%d %d", &A, &B);
    
    A--;
    B--;
    
    rowA = A % 4 + 1;
    colA = A / 4 + 1;
    
    rowB = B % 4 + 1;
    colB = B / 4 + 1;
    
    printf("%d", abs(rowA - rowB) + abs(colA - colB));
    

    return 0;
}

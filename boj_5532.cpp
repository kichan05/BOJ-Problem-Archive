#include <iostream>
#include <algorithm> 

using namespace std;


int main() {
  int L, A, B, C, D;

  scanf("%d", &L);
  scanf("%d", &A);
  scanf("%d", &B);
  scanf("%d", &C);
  scanf("%d", &D);

  while(A > 0 || B > 0){
    if(A >= C) A -= C;
    else if(A > 0) A = 0;

    if(B >= D) B -= D;
    else if(B > 0) B = 0;
    
    L--;
  }

  printf("%d", L);
  
}

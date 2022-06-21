#include <iostream>
#include <algorithm> 

using namespace std;


int main() {
  int max = -1, iMax, jMax, n;
  
  for(int i = 1; i <= 9; i++){
    for(int j = 1; j <= 9; j++){

      scanf("%d", &n);

      if(max < n){
        max = n;
        iMax = i;
        jMax = j;
      }
      
    }
  }

  
  printf("%d\n", max);
  printf("%d %d", iMax, jMax);
}

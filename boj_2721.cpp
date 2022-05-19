#include <iostream>
#include <algorithm> 
#include <cmath>

using namespace std;

int main() {
  int T, n, sum = 0, s = 0;


  scanf("%d", &T);

  while(T--){
    sum = 0;
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
      for(int j = 1; j <= i + 1; j++){
        // printf("%d, %d\n", i, j);
        sum += i * j;
      }
    }
  
    printf("%d\n", sum);
  }
}

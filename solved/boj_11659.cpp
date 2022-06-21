#include <iostream>
#include <algorithm>

using namespace std;

int sums[100001] = {};

int main(){
  int N, M;

  scanf("%d %d", &N, &M);

  for(int i = 1; i <= N; i++){
    int n;

    scanf("%d", &n);

    sums[i] = sums[i - 1] + n;
  }

  // for(int i = 1; i <= N; i++){
  //   printf("%d\n", sums[i]);
  // }

  while(M--){
    int i, j;

    scanf("%d %d", &i, &j);
    printf("%d\n", sums[j] - sums[i - 1]);
  }
  
  return 0;
}

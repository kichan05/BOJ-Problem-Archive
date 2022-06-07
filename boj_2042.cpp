#include <iostream>
#include <algorithm>

using namespace std;

int sums[100001] = {};
int nums[100001] = {};
int diffValue[10001] = {};

int main(){
  int N, M, K;

  scanf("%d %d %d", &N, &M, &K);

  for(int i = 1; i <= N; i++){
    int n;

    scanf("%d", &n);

    nums[i] = n;
    sums[i] = sums[i - 1] + n;
  }

  for(int i = 0; i < M + K; i++){
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);


    if(a == 1){
      diffValue[b] += c - nums[b];
      

      nums[b] = c;
    }
    else{
      int sum = sums[c] - sums[b - 1];
      for(int j = b; j <= c; j++)
        sum += diffValue[j];
      
      printf("%d\n", sum);
    }
  }
  
  return 0;
}

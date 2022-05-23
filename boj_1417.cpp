#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int N, my, maxidx, sum = 0;
  int counts[51] = { 0 };

  scanf("%d", &N);
  scanf("%d", &my);
  
//   _my = my;
  
  for(int i = 0; i < N - 1; i++)
    scanf("%d", counts + i);

  if(N != 1)
    sort(counts, counts + N - 1, greater<>());

  while(my <= counts[0] && N != 1){
    my++;
    sum++;
    counts[0]--;
    
    sort(counts, counts + N - 1, greater<>());
  }

  printf("%d", sum);
    
}

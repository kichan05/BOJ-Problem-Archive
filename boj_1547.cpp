#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  // int cups[] = {1, 2, 3};
  int temp = 1, M, x, y;

  scanf("%d", &M);

  while(M--){
    scanf("%d %d", &x, &y);
    if(x == temp) temp = y;
    else if(y == temp) temp = x;
    // temp = cups[x];
    // cups[x] = cups[y];
    // cups[y] = temp;
  }

  printf("%d", temp);
}

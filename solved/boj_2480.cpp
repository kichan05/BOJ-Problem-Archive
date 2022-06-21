#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int a, b, c, muney;

  scanf("%d %d %d", &a, &b, &c);
  
  switch((a == b) + (b == c) + (a == c)){
    case 3:
    case 2:
      muney = 10000 + a * 1000;
      break;
    case 1:
      int temp;

      if (a == b) temp = a;
      else if (b == c) temp = b;
      else if(c == a) temp = a;
      
      muney = 1000 + temp * 100;
      break;
    case 0:
      int max;

      if(a > b) max = a;
      else max = b;

      if(max < c) max = c;
      
      muney = max * 100;
      break;
  }

  printf("%d", muney);
}

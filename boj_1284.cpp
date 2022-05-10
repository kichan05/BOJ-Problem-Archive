#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int n;

  scanf("%d", &n);


  while(n != 0){
    int sum = 1, n_;
    
    while(n > 0){
      n_ = n % 10;
      n /= 10;

      if(n_ == 1) sum += 2;
      else if(n_ == 0) sum += 4;
      else sum += 3;

      sum++;
      
    }
    printf("%d\n", sum);
    scanf("%d", &n);
  }
  
}

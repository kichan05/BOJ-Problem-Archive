#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    int max, min;
    
    scanf("%d %d %d", &a, &b, &c);
    
    if(a < b){
        max = b;
        min = a;
    }
    else{
        max = a;
        min = b;
    }
        
    if(max < c)
        max = c;
    if(min > c)
        min = c;


    printf("%d %d %d", min, a + b + c - max - min, max);

    return 0;
}

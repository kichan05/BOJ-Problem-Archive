#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str = "SciComLove";
    
    int N;
    scanf("%d", &N);
    
    N %= 10;
    for (int i = N; i < 10; i++)
        printf("%c", str[i]);
        
    for (int i = 0; i < N; i++)
        printf("%c", str[i]);

    return 0;
}

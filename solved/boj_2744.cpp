#include <iostream>

using namespace std;

int main(){
    char str[101];
    
    scanf("%s", str);
    
    for(int i = 0; str[i]; i++){
        if('a' <= str[i] && str[i] <= 'z') printf("%c", str[i] - 32);
        else printf("%c", str[i] + 32);
    }
    

    return 0;
}

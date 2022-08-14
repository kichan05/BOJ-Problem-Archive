#include <iostream>

using namespace std;

char str[3001];
int isCap = 0;
int count = 0;

int main(){
    scanf("%s", str);
    
    for(int i = 0; str[i] != NULL; i++){
        if(isCap == 0 && 'A' <= str[i] && str[i] <= 'Z'){
            count++;
            if(str[i + 1] != NULL && 'A' <= str[i + 1] && str[i + 1] <= 'Z')
                isCap = 1;
        }
        else if(isCap == 1 && 'a' <= str[i] && str[i] <= 'z'){
            count++;
            if(str[i + 1] != NULL && 'a' <= str[i + 1] && str[i + 1] <= 'z')
                isCap = 0;
        }
        
        count++;
    }
    
    printf("%d", count);

    return 0;
}

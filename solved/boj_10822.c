#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
    char s[102];
    scanf("%s", s);
    int stringLength = strlen(s);
    s[stringLength] = ',';
    s[stringLength + 1] = '\0';
    
    int i = 0, sum = 0;
    int length = 0;
    while(s[i]) {
        if(s[i] == ','){
            for(int l = length - 1; l >= 0; l--) {
                sum += pow(10, l) * (s[i - l - 1] - 48);
            }
            length = 0;
        }
        else {
            length += 1;
        }
        i += 1;
    }
    printf("%d", sum);

    return 0;
}

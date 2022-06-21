#include <stdio.h>

char fun(char ch){
    if('A' <= ch && ch <= 'M'){
        ch += 13;
    }
    else if('N' <= ch && ch <= 'Z'){
        ch -= 13;
    }
    else if('a' <= ch && ch <= 'm'){
        ch += 13;
    }
    else if('n' <= ch && ch <= 'z'){
        ch -= 13;
    }
    
    return ch;
}

int main() {
    int idx = 0;
    char str[101];
    gets(str);
    
    // printf("%s", str);
    
    while(str[idx]){
        printf("%c", fun(str[idx++]));
    }
}

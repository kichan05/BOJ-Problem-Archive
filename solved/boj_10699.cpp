#include <iostream>
#include <ctime>

using namespace std;

int main(){
    time_t time_ = time(NULL);
    struct tm* t = localtime(&time_);
    
    printf("%d-%02d-%02d", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday + 1);

    return 0;
}

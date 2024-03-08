#include<iostream>
#include<cstdio>
#include <cstdlib>
#include<intrin.h>
using namespace std;



void init(){
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

void what() {
    system("whoami");
}

int main(){
    char buf[16];
    init();
    cout << "You Can not pwn me!" << endl;
    cin >> buf;
    cout << buf << endl;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    int tmp = a;
    while(1) {
        if (tmp > b) break;
        else {
            cout << tmp << ' ';
            if (tmp % 2 == 0) tmp += 3;
            else tmp *= 2;
        }
    }
    return 0;
}
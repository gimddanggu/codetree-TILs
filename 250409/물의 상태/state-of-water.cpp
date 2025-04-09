#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    string res;
    cin >> a;
    if (a < 0) res = "ice";
    else if (a >= 100) res = "vapor";
    else res = "water";

    cout << res;

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    string res;
    cin >> a;
    if (a >= 3000) res = "book";
    else if (a >= 1000) res = "mask";
    else res = "no";

    cout << res; 

    return 0;
}
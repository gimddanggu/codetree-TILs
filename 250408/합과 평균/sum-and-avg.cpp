#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int a, b;
    cin >> a >> b;
    cout << a + b << ' ';

    cout << fixed;
    cout.precision(1);

    cout << (a + b) / 2.0;

    return 0;
}
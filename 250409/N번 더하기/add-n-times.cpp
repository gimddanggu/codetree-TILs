#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    for (int i = 0; i < b; i++) {
        cout << a + (b * (i+1)) << '\n';
    }
    return 0;
}
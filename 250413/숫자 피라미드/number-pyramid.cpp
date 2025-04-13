#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin >> a;
    for (int i = 1; i < a+1; i++) {
        for (int j = 1; j <= i; j++) {
            cout << i << ' ';
        }
        cout << endl;
    }
    return 0;
}
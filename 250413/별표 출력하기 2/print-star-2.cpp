#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin >> a;
    for (int i = a; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            cout << "* ";
        }
        for (int j = a - i; j < a; j++) {
            cout << ' ';
        }
        cout << endl;
    }
    return 0;
}
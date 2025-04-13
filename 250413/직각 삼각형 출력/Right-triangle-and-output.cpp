#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin >> a;

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < i * 2 + 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
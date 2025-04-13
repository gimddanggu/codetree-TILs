#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin >> a;
    int num = 1;
    for (int i = 0; i < a; i++) {
        for (int j = 0; j <= i; j++) {
            cout << num << ' ';
            num += 1;
        }
        cout << endl;
    }
    return 0;
}
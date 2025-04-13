#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin >> a;

    for (int i = 1; i < a+1; i++) {
        for (int j = 1; j < a+1; j++) {
            cout << i << " * " << j << " = " << i*j;

            if (j < a) cout << ", ";
        }
        cout << endl;
    }
    return 0;
}
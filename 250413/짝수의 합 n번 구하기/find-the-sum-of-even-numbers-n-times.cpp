#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int a, b;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        int sum = 0;
        if ( a % 2 == 1) a += 1;

        for (int j = a; a < b+1; a += 2) {
            sum += a;
        }
        cout << sum << endl;
    }
    return 0;
}
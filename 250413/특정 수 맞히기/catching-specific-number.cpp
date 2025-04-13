#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    while(1) {
        cin >> a;
        if ( a == 25) { 
            cout << "Good";
            break;
        }

        else if (a > 25) cout << "Lower" << endl;
        else cout << "Higher" << endl;
    }
    return 0;
}
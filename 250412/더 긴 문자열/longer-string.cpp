#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string a, b;
    cin >> a >> b;

    if (a.length() > b.length()) cout << a + ' '<< a.length();
    else if( a.length() == b.length()) cout << "same";
    else cout << b + ' ' << b.length();
    return 0;
}
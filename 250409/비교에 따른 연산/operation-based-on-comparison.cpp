#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    int res;

    cin >> a >> b;
    res = (a > b) ? (a * b) : (b / a);
    cout << res; 
    return 0;
}
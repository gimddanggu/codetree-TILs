#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int y;
    cin >> y;

    string res;
    
    if (y % 4 == 0) {
        if (y % 100 == 0 && y % 400 != 0) {
            res = "false";
        } 
        else res = "true";
    
    } else {
        cout << "true";
    }
    cout << res;
    return 0;
}
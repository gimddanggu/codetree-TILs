#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    bool a;
    int b;
    cin >> a >> b;
    if (!a) {
        if (b >= 19) {cout << "MAN";}
        else {cout << "BOY";}
    } 
    else {
        if (b >= 19) cout << "WOMAN";
        else cout << "GIRL";
    
    }
    return 0;
}
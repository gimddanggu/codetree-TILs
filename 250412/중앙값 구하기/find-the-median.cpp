#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b  >> c;
    int mid = 0;
    
    if (a > b) {
        if (a < c) mid = a;
        else if ( a > c && b > c) mid = b; 
        else mid = c;
    }
    else {
        if ( b < c ) mid = b;
        else if ( b > c && a > c ) mid = a;
        else mid = c;  
    }

    cout << mid;
    return 0;
}
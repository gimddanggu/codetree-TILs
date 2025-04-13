#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int tCount = 0;
    int fCount = 0;

    for (int i = 0; i < 10; i++) cin >> arr[i];

    for (int i = 0; i < 10; i++) {
        if ( arr[i] % 3 == 0) tCount++;
        if ( arr[i] % 5 == 0) fCount++;   
    }

    cout << tCount << ' ' << fCount;

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char a;
    int count = 0;

    cin >> a;
    
    for (int j = 0; j < 5; j++) {
        for (int i = 2; i <= 3; i++) {
            if (arr[j][i] == a) {
                cout << arr[j] << endl;
                count++;
                break;  // 다음 문자열로 넘어감
            }
        }
    }

    cout << count;
    
    return 0;
}
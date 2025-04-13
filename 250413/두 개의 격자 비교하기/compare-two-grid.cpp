#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, m;
    cin >> n >> m;

    int arr1[10][10];
    int arr2[10][10];
    int res[10][10];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr1[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr2[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr1[i][j] != arr2[i][j]) {
                res[i][j] = 1;
            }
            else res[i][j] = 0;
            cout << res[i][j] << ' ';
        }
        cout << endl;
    } 


    return 0;
}
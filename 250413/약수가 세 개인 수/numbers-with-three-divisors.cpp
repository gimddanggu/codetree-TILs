#include <iostream>

using namespace std;



int main() {
    int start, end;
    int count = 2;  // 2 부터 약수 확인
    int res = 0;
    cin >> start >> end;
    
    for (int i = start; i < end+1; i++) {
        for (int j = 2; j < (i / 2) + 1; j++) {
            if (i % j == 0) {
                if (j == i / j) count += 1; // 33
                else if (i / j < j) break; //2 3 , 3 3
                else count += 2;
            }

        }
        // cout << count << ' ';
        if (count == 3) {
            res += 1;
        }
        count = 2;
    }

    cout << res;
    // Please write your code here.

    return 0;
}

#include <iostream>

using namespace std;

int main() {
    int N, M;

    cin >> N;
    cin >> M;
    
    // Please write your code here.
    cout << N << '\n';
    while(N>0) {
        N /= M;
        if (N == 0) break;
        cout << N << '\n';
    }
    
    return 0;
}

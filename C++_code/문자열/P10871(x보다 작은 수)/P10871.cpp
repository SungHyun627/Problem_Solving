#include <iostream>

using namespace std;

int main (void) {
    // C와 C++ 표준 입출력 Stream의 동기화 끊는다.
    ios_base::sync_with_stdio(false);
    // cin 사용시 출력 버퍼를 비우지(flush) 않는다.
    cin.tie(nullptr);
    freopen("./input.txt", "r", stdin);

    int n, x;
    int* a = new int[n];
    cin >> n >> x;
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0;i < n; i++) {
        if (a[i] < x) {
            cout << a[i] << ' ';
        }
    }
}
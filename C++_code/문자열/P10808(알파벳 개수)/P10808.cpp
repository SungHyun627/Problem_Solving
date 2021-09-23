#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main (void) {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    //freopen("./input.txt", "r", stdin);

    vector <int>v(26);
    string s;
    
    cin >> s;
    
    for (int i = 0; i < s.length(); i++) {
        v[int(s[i]) - int('a')] += 1;
    }

    for (int e: v) {
        cout << e << ' ';
    }
}
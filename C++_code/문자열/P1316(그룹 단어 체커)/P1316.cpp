#define _crt_secure_no_warnings
#include <bits/stdc++.h>
using namespace std;

//단어의 개수
int n;
//그룹 단어 체커
int result = 0;

bool check_group_word(string a) {
	map<char, int>check;
	for (int j = 0; j < a.size(); j++) {
		//들어있지 않은 경우
		if (check.find(a[j]) == check.end()) {
			check[a[j]] = j;
		}
		else {
			if (j - check[a[j]] == 1) check[a[j]] = j;
			else return false;
		}
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	//freopen("./input.txt", "r", stdin);
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		if (check_group_word(s)) result += 1;
	}
	cout << result;
}
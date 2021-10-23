#include <bits/stdc++.h>

using namespace std;
vector<int>v;
int n = 5;
//뽑을 개수
vector<int>temp(n);
int k = 3;

int main() {
	freopen("itertools.txt", "r", stdin);
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		v.push_back(x);
	}
	//정렬
	sort(v.begin(), v.end());

	//모든 순열 출력 (오름차순 우선)
	do {
		for (int i = 0; i < v.size() ; i++) {
			cout << v[i] << ' ';
		}
		cout << '\n';
	} while (next_permutation(v.begin(), v.end()));
	
	//n개중 k개의 조합
	fill(temp.begin(), temp.begin() + k, 0);
	fill(temp.end() - (n-k), temp.end(), 1);

	for (int i = 0; i < n; i++) {
		cout << temp[i] << " ";
	}
	cout << '\n';

	do {
		for (int i = 0; i < temp.size(); i++) {
			if (temp[i] == 0) {
				cout << v[i] << ' ';
			}
		}
		cout << '\n';
	} while (next_permutation(temp.begin(), temp.end()));
}
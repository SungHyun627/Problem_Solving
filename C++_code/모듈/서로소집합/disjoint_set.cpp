#include <bits/stdc++.h>

using namespace std;

//노드 개수, 간선
int v, e;
//부모 테이블
int parent[100001];
//간선과 비용을 담을 vector
vector<pair<int, pair<int, int>>> edges;
//최종 비용
int result = 0;

int find_parent(int x) {
	if (x == parent[x]) return x;
	return parent[x] = find_parent(parent[x]);
}

void union_parent(int a, int b) {
	a = find_parent(a);
	b = find_parent(b);
	if (a > b) parent[a] = b;
	else parent[b] = a;
}

int main() {
	freopen("disjoint_set.txt", "r", stdin);

	//노드, 간선의 수 입력
	cin >> v >> e;
	
	//테이블 상에서 부모를 자기 자신으로 초기화
	for (int i = 0; i < v; i++) {
		parent[i] = i;
	}
	
	//간선에 대한 정보 입력받기
	for (int i = 0; i < e; i++) {
		int a, b, cost;
		cin >> a >> b >> cost;
		edges.push_back({ cost, {a, b} });
	}

	//간선을 비용의 오름차순으로 정렬
	sort(edges.begin(), edges.end());

	//간선을 하나씩 확인
	for (int i = 0; i < edges.size(); i++) {
		int cost = edges[i].first;
		int a = edges[i].second.first;
		int b = edges[i].second.second;
		
		//싸이클 유무 확인
		if (find_parent(a) != find_parent(b)) {
			union_parent(a, b);
			result += cost;
		}
	}

	//비용 출력
	cout << result;
}
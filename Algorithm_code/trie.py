#트라이 알고리즘
#문자열 탐색에 용이
#가장 긴 문자열의 길이 N, 총 문자열 수 M => N*M
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        #처음 루트로 잡아준다
        cur_node = self.root 
        # 받은 문자열 하나하나에 대해서
        for c in s: 
            # 현재 노드에 그 문자가 있으면 들어가고, 그렇지 않으면 새로 만든다
            if c not in cur_node: 
                cur_node[c] = {}
            cur_node = cur_node[c]
        # "*" 노드를 만들어 '단어의 끝' 표시를 해 준다.
        cur_node["*"] = s 

    def search(self, s):
        cur_node = self.root
        for c in s:
            if c in s:
                cur_node = cur_node[c]
            else:
                return False
        # "*" 가 해당 노드에 있으면 그 글자로 끝나는 단어가 있다는 것이다.
        return "*" in cur_node 
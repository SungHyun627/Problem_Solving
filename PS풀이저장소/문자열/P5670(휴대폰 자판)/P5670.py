from sys import stdin

stdin = open('./input.txt', 'r')

#트라이 알고리즘
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node["*"] = s
    
    def input_count(self, s):
        count = 0
        cur_node = self.root
        # print(cur_node)
        for c in s:
            cur_node = cur_node[c]
            if "*" in cur_node or len(cur_node) >= 2:
                count += 1
        
        return count


while True:
    t = stdin.readline()
    #버튼을 누르는 총 횟수
    total_count = 0

    if not t:
        break

    trie = Trie()
    words = []
    for _ in range(int(t)):
        s = stdin.readline().rstrip()
        words.append(s)
        trie.insert(s)
    
    for i in range(int(t)):
        # print("word", words[i], trie.input_count(words[i]))
        total_count += trie.input_count(words[i])
    
    print('{0:.2f}'.format(total_count / int(t)))
n = int(input())
sequences = list(set(input() for _ in range(n)))

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
                cur_node = cur_node[c]
        cur_node['*'] = s

    
    def search(self, s):
        cur_node = self.root
        for c in s:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                return False
        if len(cur_node) != 1:
            return True
        else:
            if '*' in cur_node:
                return False
            return True

sequences.sort(lambda x: (len(x), x))

def check():
    t = Trie()
    seq_len = len(sequences)
    for i in range(seq_len-1, -1, -1):
        s = sequences[i]
        if t.search(s):
            return True
        t.insert(s)
    return False

print(0 if check() else 1)
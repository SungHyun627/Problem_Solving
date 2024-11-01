const s = 'abc';

class Node {
  constructor(value = '') {
    this.value = value;
    this.children = new Map();
    this.end = false;
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(s) {
    let curNode = this.root;

    for (let c of s) {
      if (!curNode.children.has(c)) curNode.children.set(c, new Node(c + curNode.value));
      curNode = curNode.children.get(c);
    }
    this.end = true;
  }
  search(s) {
    let curNode = this.root;

    for (let c of s) {
      if (!curNode.children.has(c)) return false;
      curNode = curNode.children.get(c);
    }
    return true;
  }
}

const t = new Trie();

t.insert('abc');
t.insert('afdfs');
t.insert('123');
console.log(t.search('a'));

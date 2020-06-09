class Trie(object):
    def __init__(self):
        self.root = {}

    def add(self, word):
        d = self.root
        for c in word:
            d = d.setdefault(c, {})
        d[None] = None

    def prefix(self, word):
        d = self.root
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return True

    def contains(self, word):
        d = self.root
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return None in d


if __name__ == "__main__":
    trie = Trie()
    trie.add("cat")
    trie.add("camel")
    trie.add("cow")
    trie.add("dog")

    assert trie.prefix("")
    assert trie.prefix("c")
    assert trie.prefix("ca")
    assert trie.prefix("came")
    assert trie.prefix("camel")
    assert trie.prefix("d")
    assert trie.prefix("dog")
    assert not trie.prefix("e")
    assert not trie.prefix("cc")

    assert trie.contains("cow")
    assert trie.contains("camel")
    assert trie.contains("dog")
    assert not trie.contains("cam")
    assert not trie.contains("cc")

    print("Done")

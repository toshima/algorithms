# indexes
#       0
# 1  2    4      8
#    3   5 6   9 10 12
#          7     11


class FenwickTree(object):
    def __init__(self, size):
        self.data = [0] * size

    def update(self, i, x):
        while i <= len(self.data):
            self.data[i - 1] += x
            i += i & (-i)

    # query prefix sum up to and including index i
    def query(self, i):
        x = 0
        while i > 0:
            x += self.data[i - 1]
            i -= i & (-i)
        return x


if __name__ == "__main__":
    ft = FenwickTree(6)
    ft.update(1, 8)
    ft.update(2, 4)
    ft.update(3, 2)
    ft.update(5, 20)
    assert ft.query(0) == 0
    assert ft.query(1) == 8
    assert ft.query(2) == 12
    assert ft.query(3) == 14
    assert ft.query(4) == 14
    assert ft.query(5) == 34
    print("Done")

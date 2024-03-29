# indexes
#    1
#  2   3
# 4 5 6 7


class SegmentTree(object):
    def __init__(self, size, initial=float("-inf"), func=max):
        from math import ceil, log2

        self.offset = 1 << ceil(log2(size))
        self.data = [initial] * (2 * self.offset)
        self.initial = initial
        self.func = func

    # update value at index i
    def update(self, i, x):
        i += self.offset
        while i:
            self.data[i] = self.func(self.data[i], x)
            i >>= 1

    # query max between indexes i and j inclusive
    def query(self, i, j):
        i += self.offset
        j += self.offset + 1
        ans = self.initial
        while i < j:
            if i & 1:
                ans = self.func(ans, self.data[i])
                i += 1
            if j & 1:
                j -= 1
                ans = self.func(ans, self.data[j])
            i >>= 1
            j >>= 1
        return ans


if __name__ == "__main__":
    st = SegmentTree(5)
    st.update(0, 5)
    st.update(1, 8)
    st.update(2, 4)
    st.update(3, 2)
    st.update(4, 20)
    assert st.query(0, 0) == 5
    assert st.query(0, 3) == 8
    assert st.query(0, 4) == 20
    assert st.query(1, 4) == 20
    assert st.query(1, 3) == 8
    assert st.query(2, 3) == 4
    assert st.query(4, 4) == 20
    assert st.query(1, 0) == -float("inf")
    print("Done")

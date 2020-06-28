
class MinQueue(object):
    def __init__(self):
        from collections import deque
        self.q = deque()

    def push(self, x):
        count = 1
        while self.q and self.q[-1][0] > x:
            count += self.q.pop()[1]
        self.q.append([x, count])

    def pop(self):
        self.q[0][1] -= 1
        if not self.q[0][1]:
            self.q.popleft()

    def min(self):
        return self.q[0][0]


if __name__ == '__main__':
    mq = MinQueue()
    mq.push(3)
    assert mq.min() == 3
    mq.push(3)
    assert mq.min() == 3
    mq.push(1)
    assert mq.min() == 1
    mq.push(4)
    assert mq.min() == 1
    mq.pop()
    assert mq.min() == 1
    mq.pop()
    assert mq.min() == 1
    mq.push(2)
    assert mq.min() == 1
    mq.pop()
    assert mq.min() == 2
    print("Done")


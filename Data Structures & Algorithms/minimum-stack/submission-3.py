class MinStack:

    def __init__(self):
        self.st = []
        self.mst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.mst: self.mst.append(min(self.mst[-1], val))
        else: self.mst.append(val)

    def pop(self) -> None:
        self.mst.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1]

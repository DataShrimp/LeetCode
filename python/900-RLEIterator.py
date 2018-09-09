class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        # decode, memory error
        self.ret_list = []
        for i in range(0, len(A), 2):
            self.ret_list.append(A[i]*[A[i+1]])
        # trick
        self.ret_list = sum(self.ret_list, [])
        print(self.ret_list)
        # iterator, for next2() function
        self.ret_iter = iter(self.ret_list)
        # pointer, for next() function
        self.ptr = 0

    def next(self, n):
        if self.ptr+n-1 < len(self.ret_list):
            ret = self.ret_list[self.ptr+n-1]
            self.ptr += n
            return ret
        else:
            return -1

    def next2(self, n):
        """
        :type n: int
        :rtype: int
        """
        try:
            for i in range(n-1):
                next(self.ret_iter)
            return next(self.ret_iter)
        except StopIteration:
            return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

if __name__ == "__main__":
    rle = RLEIterator([3,8,0,9,2,5])
    print(rle.next(2))
    print(rle.next(1))
    print(rle.next(1))
    print(rle.next(2))

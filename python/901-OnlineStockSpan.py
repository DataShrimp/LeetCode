class StockSpanner:

    def __init__(self):
        self.A = []

    # misunderstand, return the tail N number
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ret = 1
        count = 0
        for i in range(len(self.A)):
            if price <= self.A[i]:
                self.A.insert(i, price)
                count = i
                break
            else:
                count = i+1
            if i == len(self.A) - 1:
                self.A.append(price)
                break
        ret += count
        if len(self.A) == 0:
            self.A.append(price)
        return ret

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == "__main__":
    s = StockSpanner()
    print(s.next(29))
    print(s.next(91))
    print(s.next(62))
    print(s.next(76))
    print(s.next(51))

class Solution:
    def swap(self, w, i, j):
        temp = w[i]
        w[i] = w[j]
        w[j] = temp

    def get_permutation(self, w, start, end):
        if start >= end:
            print(w)
        else:
            i = start
            for num in range(start, end):
                self.swap(w, i, num)
                self.get_permutation(w, start+1, end)
                self.swap(w, i, num)


if __name__ == "__main__":
    Solution().get_permutation([1,2,3], 0, 3)
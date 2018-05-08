class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S.find("@") > 0:
            ret = self.maskEmail(S)
        else:
            ret = self.maskPhone(S)
        return ret

    def maskEmail(self, S):
        str = S.lower()
        loc = str.find("@")
        str = str[0] + "*"*5 + str[loc-1] + str[loc:]
        return str

    def maskPhone(self, S):
        S=S.replace("(", "")
        S=S.replace(")", "")
        S=S.replace("+", "")
        S=S.replace("-", "")
        S=S.replace(" ", "")
        str = "*"*3 + "-" + "*"*3 + "-" + S[-4:]
        l = len(S)
        if l > 10:
            str = "+" + "*"*(l-10) + "-" + str
        return str



if __name__ == "__main__":
    S = "86-(10)12345678"
    print(Solution().maskPII(S))
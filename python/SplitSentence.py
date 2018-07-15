dp = [[-1]*10 for i in range(10)]


def split_sentence(s, i, j, word_dict):
    global dp
    if dp[i][j] == -1:
        dp[i][j] = word_dict.get(s[i:j], 0)
    if j-i == 1:
        return dp[i][j]
    temp = list()
    temp.append(dp[i][j])
    for k in range(i+1, j):
        temp.append(split_sentence(s, i, k, word_dict) + split_sentence(s, k, j, word_dict))
    dp[i][j] = max(temp)
    #if dp[i][j] is not temp[0]:
    #    print(temp.index(dp[i][j]), dp[i][j])
    return dp[i][j]


if __name__ == "__main__":
    word_dict = {'abc':10, 'de':10, 'abcde':12}
    sentence = 'abcde'
    split_sentence(sentence, 0, len(sentence), word_dict)
    for i in range(len(dp)):
        print(dp[i])

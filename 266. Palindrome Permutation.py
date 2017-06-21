def canPermutePalindrome(self, s):
    dic = {}
    for item in s:
        dic[item] = dic.get(item, 0) + 1
    # return sum(v % 2 for v in dic.values()) < 2
    count1 = 0
    for val in dic.values():
        if val % 2 == 1:
            count1 += 1
        if count1 > 1:
            return False
    return True
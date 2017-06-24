class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        tmp = list(secret);
        correct = [False for _ in range(len(secret))];
        
        for i, c in enumerate(guess):
            if c in tmp:
                tmp.remove(c);
            correct[i] = c==secret[i];
        
        return str(sum(correct))+'A'+str(len(secret)-len(tmp)-sum(correct))+'B'


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)
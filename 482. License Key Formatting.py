class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '');
        i = len(S);
        result = ''
        while i>0:
            j = max(0, i-K);
            result ='-'+S[j:i].upper()+result;
            i = j;
        return result[1:]
            
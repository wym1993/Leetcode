class Solution(object):
    def findStrobogrammatic(self, n):
        result = []
        hash = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        self.helper(result, [None]*n, 0, n-1, hash)

        return result

    def helper(self, result, item, start, end, hash):
        if start > end:
            result.append(''.join(item))
            return

        for key in hash:
            if start == end and key in ('6','9'):
                continue

            if start != end and start == 0 and key == '0':
                continue

            item[start], item[end] = key, hash[key]
            self.helper(result, item, start+1, end-1, hash)

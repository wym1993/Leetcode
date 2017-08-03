def generatePossibleNextMoves(self, s):
    return [s[:i] + "--" + s[i + 2:] for i in xrange(len(s) - 1) if s[i:i + 2] == '++']

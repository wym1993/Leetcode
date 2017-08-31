import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = collections.Counter(moves);
        return not (counter['L']-counter['R']) and not (counter['U']-counter['D']);
        
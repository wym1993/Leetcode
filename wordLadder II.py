from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if beginWord==endWord:
            return []
        if not endWord in wordList:
            return [];
        
        wordSet = set(wordList)
        length = 0;
        level = set([beginWord]);
        parent = defaultdict(set)
        while level:
            nxt_level = set();
            nxt_parent = defaultdict(set)
            for node in level:
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        if (node[:i]+c+node[i+1:]) in wordSet:
                            nxt_level.add(node[:i]+c+node[i+1:])
                            nxt_parent[node[:i]+c+node[i+1:]].add(node)
            length+=1;
            level = nxt_level;
            parent.update(nxt_parent);
            if endWord in parent:
                break;
            wordSet-=level;
        
        result = [[endWord]];
        while result and result[0][0]!=beginWord:
            result = [[p]+r for r in result for p in parent[r[0]]]
        return result;
        
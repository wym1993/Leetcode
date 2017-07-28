class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for c, p in zip(pid, ppid): d[p].append(c)
        bfs = [kill]
        for i in bfs: bfs.extend(d.get(i, []))
        return bfs
            
        
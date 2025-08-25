from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            start = 0
            wordList = [beginWord]+wordList
        else:
            start = wordList.index(beginWord)

        m = len(wordList)

        # w_to_i = {i:wordList[i] for i in range(len(wordList))} 
        # i_to_w = {wordList[i]:i for i in range(len(wordList))}

        adj_list = {i:[] for i in range(m)}

        def diff(w1,w2):
            not_same = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    not_same += 1
                if not_same > 1:
                    return not_same
            return not_same
        
        for i in range(m):
            for j in range(i+1,m):
                if diff(wordList[i], wordList[j]) == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        
        def bfs(ind):
            visited = [ind]
            q = deque()
            next_q = deque()
            q.append(ind)
            count = 1
            while(q or next_q):
                curr = q.popleft()
                for j in adj_list[curr]:
                    if wordList[j] == endWord:
                        return count+1
                    if j not in visited:
                        visited.append(j)
                        next_q.append(j)
                if not q:
                    count += 1
                    q = next_q.copy()
                    next_q = deque()

            return 0

        return bfs(start)


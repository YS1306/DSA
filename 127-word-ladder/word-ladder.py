from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList = [beginWord]+wordList
        m = len(wordList)
        
        for i in range(m):
            if wordList[i] == beginWord:
                start = i
                break

        

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
        
        
        visited = [0 for i in range(m)]
        q = deque()
        next_q = deque()
        q.append(start)
        count = 1
        while(q or next_q):
            curr = q.popleft()
            for j in adj_list[curr]:
                if wordList[j] == endWord:
                    return count+1
                if not visited[j]:
                    visited[j] = 1
                    next_q.append(j)
            if not q:
                count += 1
                q = next_q.copy()
                next_q = deque()

        return 0



class Solution {
private:
    bool backtracking(string &s, string &current, vector<string> &wordDict, unordered_set<string> &visited)
    {
        if (visited.count(current) ||
            current.length() > s.length() ||
            (current.length() > 0 && s.find(current) != 0)) return false;
        if (current == s) return true;
        visited.insert(current);
        for (const auto &word: wordDict)
        {
            current += word;
            if (backtracking(s, current, wordDict, visited)) return true;
            current.erase(current.length() - word.length());
        }
        return false;
    }
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        string current;
        unordered_set<string> visited;
        return backtracking(s, current, wordDict, visited);
    }
};
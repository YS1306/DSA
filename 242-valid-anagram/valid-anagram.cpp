class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_cnt;
        if(s.size() != t.size())    return false;
        int n = s.size();
        for(int i=0; i<n; i++){
            s_cnt[s[i]]++;
            s_cnt[t[i]]--;
        }
        for(auto i:s_cnt){
            if(i.second != 0)   return false;
        }
        return true;
    }
};
class Solution {
public:
    int ans = 0;
    int beautySum(string s) {

        for (int i = 0; i < s.length()-1; i++) {
            unordered_map<char, int> mp;
            mp[s[i]]++;
            for (int j = i+1; j < s.length(); j++) {
                // counting the frequency of each character
                mp[s[j]]++;
                int leastFrequent = INT_MAX;
                int mostFrequent = INT_MIN;
                // Finding most frequent and least frequent chracter
                for (auto it : mp) {
                    leastFrequent = min(leastFrequent, it.second);
                    mostFrequent = max(mostFrequent, it.second);
                }
                ans += mostFrequent - leastFrequent;
            }
        }

        return ans;
    }
};
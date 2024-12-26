class Solution {
public:
    static bool cmp(pair<char, int>& a, pair<char, int>& b) 
    { 
        return a.second > b.second; 
    } 

    string frequencySort(string s) {
        int n = s.size();
        string res;
        unordered_map<char, int> count;
        for(int i=0; i<n; i++){
            count[s[i]]++;           
        }

        vector<pair<char, int>> A;     
        for (auto& it : count) { 
            A.push_back(it); 
        } 
        sort(A.begin(), A.end(), cmp); 
        for(auto it : A){
            for(int j=0; j<it.second; j++)   res.push_back(it.first);    
        }
        return res;
    }

};
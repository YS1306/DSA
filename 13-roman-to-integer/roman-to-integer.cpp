class Solution {
public:
    int romanToInt(string s) {
        int n = s.size();
        int i=n-2;
        unordered_map<char, int> values = { {'I',1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M',1000} };
        int res=0;
        int temp = values[s[n-1]];
        char prev = s[n-1];
        while(i >= 0){
            char curr = s[i];
            if(values[curr] < values[prev]){
                temp -= values[curr];
            }
            else if(values[curr] >= values[prev]){
                res += temp;
                temp = values[curr];
                prev = curr;
            }
            i--;
        } 
        return res+temp;    
    }


};
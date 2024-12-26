class Solution {
public:
    int maxDepth(string s) {
        int n = s.size();
        vector<char> stack;
        int top = 0, res  = 0;
        for(int i=0; i<n; i++){
            if(s[i] == '('){
                stack.push_back('(');
                top++;
            }     
            else if(s[i] == ')'){
                res = max(res, top);
                stack.pop_back();
                top--;
            }
        }
        return res;   
    }
};
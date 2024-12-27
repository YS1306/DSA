class Solution {
public:
    int romanToInt(string s) {
        int i=0;
        unordered_map<char, int> priority = { {'I',1}, {'V', 2}, {'X', 3}, {'L', 4}, {'C', 5}, {'D', 6}, {'M',7} };
        unordered_map<char, int> values = { {'I',1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M',1000} };
        vector<char> stack;
        int res=0;
        int top=-1;
        while(s[i] != '\0'){
            if(top == -1){  stack.push_back(s[i]);  top++;}
            else{
                if(priority[s[i]] > priority[stack[top]]){
                    stack.push_back(s[i]); top++;
                }
                else if(priority[s[i]] == priority[stack[top]]){
                    res += 2*values[s[i]];
                    stack.pop_back();
                    top--;                }
                else{
                    int temp = values[stack[top]];
                    stack.pop_back();
                    top--;
                    while(top >= 0){
                        temp -= values[stack[top]];
                        stack.pop_back();
                        top--;
                    }
                    res += temp;
                    stack.push_back(s[i]);
                    top++;
                }
            }
            i++;
        } 
        if(top == -1)   return res;
        int temp = values[stack[top]];  top--;     
        while(top >= 0){
            temp -= values[stack[top]];
            stack.pop_back();
            top--;
        }
        res += temp;
        return res;
    }


};
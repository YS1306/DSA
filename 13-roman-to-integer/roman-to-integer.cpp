class Solution {
public:
    int romanToInt(string s) {
        int i=0;
        unordered_map<char, pair<int, int>> values = { {'I',{1,1}}, {'V', {2,5}}, {'X', {3, 10}}, {'L', {4,50}}, {'C', {5,100}}, {'D', {6, 500}}, {'M',{7,1000}} };
        vector<char> stack;
        int res=0;
        int top=-1;
        while(s[i] != '\0'){
            if(top == -1){  stack.push_back(s[i]);  top++;}
            else{
                pair<int, int> last = values[stack[top]];
                pair<int, int> curr = values[s[i]];
                if(curr.first > last.first){
                    stack.push_back(s[i]); top++;
                }
                else if(curr.first == last.first){
                    res += 2*last.second;
                    stack.pop_back();
                    top--;                }
                else{
                    int temp = last.second;
                    stack.pop_back();
                    top--;
                    while(top >= 0){
                        temp -= values[stack[top]].second;
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
        int temp = values[stack[top]].second;  top--;     
        while(top >= 0){
            temp -= values[stack[top]].second;
            stack.pop_back();
            top--;
        }
        res += temp;
        return res;
    }


};
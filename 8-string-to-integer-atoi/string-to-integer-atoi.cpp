class Solution {
public:
    int myAtoi(string s) {
        bool flag=false;
        bool neg=false;
        int res = 0;
        int i = 0;
        while(s[i] != '\0'){
            if(!flag){
                if(s[i] == ' '){    i++;     continue;}
                if(s[i] == '+'){     neg = false;   flag=true; }
                else if(s[i] == '-'){     flag=true;     neg=true;   }
                else if(s[i] >= 48 && s[i] <= 57){
                    flag = true;    
                    res = int(s[i])-48;
                }   
                else    return res;
            }
            else{
                if(s[i] == '0' && res == 0){    i++;    continue; }
                else if(s[i] >= 48 && s[i] <= 57){
                    if(!neg && ((INT_MAX/10) == res) && (int(s[i])-48) < 7 && s[i+1] == '\0')     return 10*res+(int(s[i])-48);    
                    else if(!neg && ((INT_MAX/10)-res) <= (int(s[i])-48))  return INT_MAX;
                    else if(neg && (INT_MAX/10 == res) && (int(s[i])-48)<8 && s[i+1] == '\0') return  -1*(10*res+(int(s[i])-48));
                    else if(neg && ((INT_MAX/10-res) <= (int(s[i])-47))){    return INT_MIN; }
                    else{    res = res*10+int(s[i])-48; }
                }
                else  break;
            }
            i++;
        }
        if(neg) return -1*res;
        return res;
    }
};
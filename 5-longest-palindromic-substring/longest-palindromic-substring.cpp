class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length(), index = 0, maxLength = 1, i = 0;

        if (n <= 1){
            return s;
        }

        while (i < n && n - i > maxLength / 2) {
            int j = i, k = i;

            while (k < n - 1 && s[k + 1] == s[k]){
                k++;
            }
            
            i = k + 1;
            
            while (k < n - 1 && j > 0 && s[k + 1] == s[j - 1]) { 
                k++; 
                j--; 
            }
            
            if (maxLength < k - j + 1) { 
                index = j;
                maxLength = k - j + 1;
            }
        }

        return s.substr(index, maxLength);
    }
};
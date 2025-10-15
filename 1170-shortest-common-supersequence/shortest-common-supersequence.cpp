class Solution {
public:
    string shortestCommonSupersequence(string word1, string word2) {
        int n = word1.size(), m = word2.size();

        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(word1[i-1] == word2[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        string lcs(dp[n][m], 'a');
        
        int i = n, j = m;
        int ind = dp[n][m]-1;
        while(i > 0 and j > 0){
            if(word1[i-1] == word2[j-1]){
                lcs[ind] = word1[i-1];
                i--;    j--;    ind--;
            }
            else{
                if(dp[i-1][j] > dp[i][j-1]){
                    i--;
                }
                else
                    j--;
            }
        }
        
        i = 0;
        j = 0;
        int k = 0;
        string res = "";
        while( i < n && j < m && k < dp[n][m]){
            // cout<<"i"<<"\t"<<i<<"\t"<<"j"<<"\t"<<j<<"\t"<<"k"<<"\t"<<k<<endl;
            if(word1[i] == word2[j] && word1[i] == lcs[k]){
                res += word1[i];
                i++;    j++;    k++;
            }
            else{
                if(word1[i] != lcs[k]){
                    res += word1[i]; i++;
                }
                if(word2[j] != lcs[k]){
                    res += word2[j]; j++;
                } 
            }

        }
        while(i < n){
            res += word1[i]; 
            i++;
        }
        while(j < m){
            res += word2[j]; 
            j++;
        }
        return res;
    }
};
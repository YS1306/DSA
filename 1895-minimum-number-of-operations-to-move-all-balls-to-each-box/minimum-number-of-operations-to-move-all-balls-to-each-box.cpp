class Solution {
public:
    vector<int> minOperations(string boxes) {
        int i = 0;
        vector<int> res;
        int count = 0;
        for(int i = 0; i< boxes.size(); i++){
            count = 0;
            for(int j = 0; j < boxes.size(); j++){
                if(boxes[j] == '1')   count += max((i-j),(j-i));
            }
            res.push_back(count);
        }
        return res;
    }
};
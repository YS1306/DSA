class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        letters = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}

        def check(rem, curr, letters):
            
            if len(rem) == 0:
                if curr not in res:
                    res.append(curr)
                return
            
            for let in letters[int(rem[0])]:
                check(rem[1:], curr+let, letters)
            
        check(digits, "", letters)
        return res
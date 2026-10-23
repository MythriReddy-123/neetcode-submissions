class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                strs += i.lower()
        print(strs)
        return strs == strs[::-1]

        
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())

        start = 0
        end = len(clean) - 1
        palindrome = True
        while(start < end):
            if clean[start] != clean[end]:
                palindrome = False
            start +=1
            end-=1

        return palindrome
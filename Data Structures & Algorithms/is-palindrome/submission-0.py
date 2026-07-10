class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch.lower()
        return result[::-1]==result
           
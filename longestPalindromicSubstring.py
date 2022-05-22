
#5. Longest Palindromic Substring

class Solution:
   
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        
        for i in range(len(s)): 
            
            # this is for odd length palindrome
            word1 = self.checkPalindrome(s, i, i)

            # this is for even length palindrome
            word2 = self.checkPalindrome(s, i, i+1)
    
            # Compare word1 & word2 & find the longerWord
            longerWord = word1 if len(word1) > len(word2) else word2
        
            # Compare longerWord with our previously obtained longerWord
            result = longerWord if len(longerWord) > len(result) else result

            print("Word 1: ", word1)
            print("Word 2: ", word2)
            print("Longer Word: ", longerWord)
            print("Result: ", result)

        return result
    
    
    def checkPalindrome(self, s, l, r):  
        # expand as long as 'l' can grow to the left
        # and 'r' and grow to the right and characters at those index match
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            l -= 1
            r += 1    
            
        # return the slice from original string that starts from our last matched index of l and r. 
        # We don't increament r because python slice goes up to ending index-1
        print("Start:", l+1)
        print("End", r)
        return s[l+1:r]


if __name__ == "__main__":
    s = "babad"
    objectNums = Solution()
    print(objectNums.longestPalindrome(s))
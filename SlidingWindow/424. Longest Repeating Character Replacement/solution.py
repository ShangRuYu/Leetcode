class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        mostChar = 0

        for right in range(len(s)):
            # count the frequency of the current character, add 1 to the count of the current character
            count[s[right]] = 1 + count.get(s[right], 0)

            # update the most frequent character count in the current window
            mostChar = max(mostChar, count[s[right]])

            # if the current window size minus the count of the most frequent character is greater than k, 
            # it means we need to shrink the window from the left
            while (right - left + 1) - mostChar > k:
                count[s[left]] -= 1 # decrease the count of the character at the left pointer
                left += 1
            
            result = max(result, right - left + 1)

        return result


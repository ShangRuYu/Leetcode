# Set approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0   # 
        result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left]) # Remove the leftmost character from the set and move the left pointer to the right
                left += 1 # Move the left pointer to the right
            seen.add(s[right]) # Add the current character to the set
            result = max(result, right - left + 1) # Update the result with the maximum length of the substring found so far
        return result

# Hashmap approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            # Only jump if duplicate is within current window
            if s[right] in charMap and charMap[s[right]] >= left:
                # move the left pointer to the right of the last occurrence of the current character
                left = charMap[s[right]] + 1
            charMap[s[right]] = right  # track the most recent index of each character
            result = max(result, right - left + 1)
        return result
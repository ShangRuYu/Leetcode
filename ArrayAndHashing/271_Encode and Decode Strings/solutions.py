class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s # We concatenate the length of the string, a delimiter "#", and the string itself to create the encoded representation.
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # Extract the length of the string by taking the substring from index i to j and converting it to an integer.
            result.append(s[j + 1: j + 1 + length]) # Extract the original string by taking the substring from index j + 1 to j + 1 + length and append it to the result list.    
            i = j + 1 + length # Update the index i to point to the next encoded string by moving past the current string and its length information.
        return result

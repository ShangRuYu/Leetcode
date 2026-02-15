class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1  # count.get(num, 0) returns the current count of num, or 0 if num is not in the count dictionary.
                                                # Then we add 1 to it to update the count for that num.

        buckets = [[] for i in range(len(nums) + 1)] #  Create a list of empty lists where the index represents the frequency of the numbers.
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                
        
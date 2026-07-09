class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # empty set to track numbers we've already seen
        
        for num in nums:
            if num in seen:      # have we seen this number before?
                return True       # yes -> it's a duplicate
            seen.add(num)         # no -> remember it for next time
        
        return False  # went through everything, no duplicates found
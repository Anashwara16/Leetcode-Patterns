
# 78. Subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subset = []
        result = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)            

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result
        

if __name__ == "__main__":
    nums = [1,2,3]
    objectNums = Solution()
    print(objectNums.subsets(nums))
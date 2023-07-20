class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]].append(i)
            else:
                mydict[nums[i]] = [i]
        nums.sort()
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] == target:
                if nums[i] != nums[j]:
                    return [mydict[nums[i]][0],mydict[nums[j]][0]]
                else:
                    return mydict[nums[i]]
            else:
                i += 1
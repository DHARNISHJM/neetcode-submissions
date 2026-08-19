class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res_index = -1;
        l,r = 0, len(nums)-1
        

        while l <= r:
            m = (l+r)//2

            if target == nums[m]:
                    res_index = m
                    break

            #When the middle element is in the left part of the array
            if (nums[m] >= nums[l]):
                # If the target is is less than nums[m]
                if (target < nums[m]):
                    if (target < nums[l]):
                        l = m+1
                    else:
                        r = m-1
                else:
                    l = m+1
            else:
                if (target > nums[m]):
                    if (target > nums[r]):
                        r = m-1
                    else:
                        l = m+1
                else:
                    r = m-1

                

        return res_index
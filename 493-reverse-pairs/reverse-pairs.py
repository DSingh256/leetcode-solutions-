class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, low, mid, high):
            ans = 0
            i,j = low,mid+1
            while(i<=mid and j<=high):
                if nums[i]>2*nums[j]:
                    ans+=(mid-i+1)
                    j+=1
                    while(j<=high and nums[i]>2*nums[j]):
                        ans+=(mid-i+1)
                        j+=1
                i+=1
            temp = []
            l, r = low, mid + 1
            while l <= mid and r <= high:
                if nums[l] <= nums[r]:
                    temp.append(nums[l])
                    l += 1
                else:
                    temp.append(nums[r])
                    r += 1

            while l <= mid:
                temp.append(nums[l])
                l += 1
            while r <= high:
                temp.append(nums[r])
                r += 1

            for i in range(low, high + 1):
                nums[i] = temp[i - low]

            return ans

        def ms(nums, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            total = ms(nums, low, mid)
            total += ms(nums, mid + 1, high)
            total += merge(nums, low, mid, high)
            return total

        return ms(nums, 0, len(nums) - 1)
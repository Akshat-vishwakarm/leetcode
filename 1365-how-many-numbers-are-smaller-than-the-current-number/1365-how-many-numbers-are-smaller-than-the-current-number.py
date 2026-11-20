class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans=[]
      
        for i in nums:
            c=0
            for j in nums:
                if j<i:
                    c+=1
            ans.append(c)
        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
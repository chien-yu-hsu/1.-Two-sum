#!/usr/bin/env python
# coding: utf-8

# In[89]:


nums = [2, 11, 7, 15]
target = 13

print(nums)


# In[90]:


num_list = list(zip(range(len(nums)), nums))
print(num_list)


# In[92]:


# solution 1 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = list(zip(nums, range(len(nums)))) 
        num_index.sort() #會依照前面的數字大小作排序


        i = 0 
        j = len(nums) - 1
        crr_sum = 0

        while i < j:
            crr_sum = num_index[i][0] + num_index[j][0]
            if crr_sum == target:
                return[num_index[i][1], num_index[j][1]] 
            elif crr_sum < target:
                i = i + 1
            else:
                j = j - 1


# In[93]:


# solution 2 #暴力解

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return[i,j]
    
        


# In[ ]:





# In[ ]:





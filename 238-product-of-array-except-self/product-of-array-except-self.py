class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        #starting point, last index value, stepping value
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        answer = []
        for i in range(n):
            answer.append(prefix[i] * suffix[i])
        return answer
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         i,answer = 0,[]
#         # to traverse over entire list
#         while (i < len(nums)):
#             # for every product a newNum starts at 1 because 1xanything is same number
#             newNum = 1
#             j = 0
#             #travese over entire list again
#             while (j < len(nums)):
#                 #if it is the nums[i] then skip
#                 if (i==j):
#                     j+=1
#                 # else just multiply it
#                 else:
#                     newNum = newNum*nums[j]
#                     j+=1
#             # saving answers in a new list
#             answer.append(newNum)
#             i+=1
#         return answer
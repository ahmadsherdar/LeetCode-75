class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        trueFalse = []
        for i in candies:
            if (extraCandies+i >= maxCandies):
                #Python has a True/False data type and instead of using string "true"/"false" simply append
                #boolean True/False T/F upper case
                 trueFalse.append(True)
            else:
                trueFalse.append(False)
        return trueFalse
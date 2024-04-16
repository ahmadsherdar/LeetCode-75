class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        totalPlots = 0
        for i in range(len(flowerbed)):
            ###make sure
            ## that current plot is empty and plotable otherwise just pass to next one
            ###make sure
            ## i is the first plot and 0 or
            ## previous plot is empty
            ### and make sure
            ## next plot is empty or
            ## this is last plot
            if flowerbed[i]==0:
                previous_plot = (i==0 or flowerbed[i-1]==0)
                next_plot = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

                if previous_plot and next_plot:
                    totalPlots+=1
                    ## without updating the list itself, the algo gets confused and still see indces as 0s 
                    ## and keeps failing so as we move forward with possible plots we plot it too
                    flowerbed[i]=1
                    if totalPlots >= n:
                        return True
        return totalPlots >= n

##
##solution_instance = Solution()
##result = solution_instance.canPlaceFlowers(flowerbed, n)
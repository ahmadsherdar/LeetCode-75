class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split()
        LS, RS = 0, len(sList)-1
        newList = []
        while (LS < len(sList)):
            newList.append(sList[RS])
            LS+=1
            RS-=1
        return " ".join(newList)
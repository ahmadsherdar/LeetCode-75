class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = j = 0
        newString = ""
        #This will add till equal length
        while i < len(word1) and j < len(word2):
            newString += word1[i]+word2[j]
            i+=1
            j+=1
        #If first string is greater then it will add remaining characters at the end
        while i < len(word1):
            newString += word1[i]
            i+=1
        #If second string is greater then it will add remaining characters at the end
        while j < len(word2):
            newString += word2[j]
            j+=1
        return newString
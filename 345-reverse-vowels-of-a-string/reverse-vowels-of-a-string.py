class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #in Python strings are immutable (not changeable) - so convert it to a list to manipulate it
        s = list(s)
        vowels = list("aeiouAEIOU")
        #defining a range for traversing
        
        LS, RS = 0, (len(s)-1)
        
        while (LS < RS):
            #find the vowel from LS
            while (LS < RS and s[LS] not in vowels):
                #if not found move to next character from left side
                LS+=1
            while (RS > LS and s[RS] not in vowels):
                #if not found move to next character from right side
                RS-=1
            #when next vowel from left and right side are found swap
            #this way it gets swapped without having to store in a third variable or losing value
            s[LS], s[RS] = s[RS], s[LS]
            
            #now main loop is incremented from left decremented from right
            LS+=1
            RS-=1
        #now our list of characters of s needs to be joined back
        return "".join(s)


        
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #if both strings do not combine to be one complete string as t+t+t..+t = it returns empty
        if str1 + str2 != str2 + str1:
            return ""
        #this will return greatest common divisor by comparing each character in both the
        #strings and return the gcd value at the end 
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        #getting gcd length
        gcd_len = gcd(len(str1), len(str2))
        #this is slicing the str1 from 0 index to gcd-1 index
        gcd_str = str1[:gcd_len]
        
        # Check if the gcd_str divides both str1 and str2, if both become '' it means they  were perfect
        if str1.replace(gcd_str, '') == '' and str2.replace(gcd_str, '') == '':
            return gcd_str
        else:
            return ""

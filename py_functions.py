class py_functions():
    
    def __init__(self):
        return None
    
    def isPalindrome(self,word):
        word = str(word).lower()
        return word==word[::-1]

    def isAnagram(self,word1,word2):
        word1=str(word1).lower()
        word2=str(word2).lower()
        return set(word1)==set(word2)

    def nearestIntPalindrome(self,num):
        num=int(num)
        i=0
        while i>=0:
            if str(num+i) == str(num+i)[::-1]:
                return str(num+i)+" is the nearest Palindrome."
                break
            elif str(num-i) == str(num-i)[::-1]:
                return str(num-i)+" is the nearest Palindrome."
                break
            else:
                i+=1

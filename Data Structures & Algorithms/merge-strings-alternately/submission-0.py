class Solution(object):
    def mergeAlternately(self, word1, word2):
        sr = ""
        a=b=0
        while a < len(word1) or b < len(word2):
            if a < len(word1):
                sr += word1[a]
                a += 1
            if b < len(word2):
                sr += word2[b]
                b += 1

        return sr
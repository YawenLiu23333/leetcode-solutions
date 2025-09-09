class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = [0] *26
        for s in sentence:
            seen[ord(s)- ord('a')] += 1
        
        for s in seen:
            if s == 0:
                return False
        
        return True
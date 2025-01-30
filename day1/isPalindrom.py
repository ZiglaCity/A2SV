class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        to_string = str(x)
        left, right = 0, len(to_string) - 1
        while left < right:
            if to_string[left] != to_string[right]:
                return False
            left += 1
            right -= 1
        return True
        
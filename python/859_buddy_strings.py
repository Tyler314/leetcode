from string import ascii_lowercase

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a_val = b_val = ""
        swapped = False
        if len(A) != len(B):
            return False
        for a_char, b_char in zip(A, B):
            if a_char != b_char:
                if swapped:
                    return False
                if a_val == b_val == "":
                    a_val = a_char
                    b_val = b_char
                elif b_char == a_val and a_char == b_val:
                    swapped = True
                else:
                    return False
        if not swapped and A == B:
            for char in ascii_lowercase:
                if A.count(char) > 1:
                    return True
        return swapped
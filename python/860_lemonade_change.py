from collections import Counter

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        valid_bills = (20, 10, 5)
        reg = Counter()
        for bill in bills:
            reg[bill] += 1
            bill -= 5
            for b in valid_bills:
                while bill >= b and reg[b] > 0:
                    bill -= b
                    reg[b] -= 1
            if bill != 0:
                return False
        return True
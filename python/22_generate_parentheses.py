class Solution:
    def __init__(self):
        self.solution_set = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.solution_set = []
        self._generateParenthesis(n, n)
        return self.solution_set
        
    def _generateParenthesis(self, o_paren, c_paren, s=''):
        if o_paren == c_paren == 0:
            self.solution_set.append(s)
            return
        if o_paren > 0:
            self._generateParenthesis(o_paren - 1, c_paren, s + '(')
        if c_paren > o_paren:
            self._generateParenthesis(o_paren, c_paren - 1, s + ')')
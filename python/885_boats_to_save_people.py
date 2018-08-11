class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        self.people = sorted(people)
        boats = 0
        while self.people:
            cnt = self.people.pop()
            val = 0
            while val != -1:
                val = self.getClosest(limit - cnt)
                if val != -1:
                    cnt += val
            boats += 1
        return boats

    def getClosest(self, num):
            """
            Assumes the list "people" is sorted
            """
            left  = 0
            right = len(self.people) - 1
            val = -1
            while left <= right:
                mid = left + ((right - left) // 2)
                val = self.people[mid]
                if val == num:
                    break
                elif val < num:
                    left = mid + 1
                elif val > num:
                    right = mid - 1
            if val > num:
                if mid == 0:
                    val = -1
                else:
                    mid -= 1
                    val = self.people[mid]
            if val != -1:
                self.people.pop(mid)
            return val
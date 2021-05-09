# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        king,check = 0,0
        numbers.sort()
        L = []
        for card in numbers:
            if card == 0:
                king+=1
            else:
                if check == card:
                    return False
                if check!=0 and card-check!=1:
                    king = king-(card-check-1)
                L.append(card)
                check = card
        if max(L)-min(L) > 4:
            return False 
        if king < 0:
            return False
        return True

sol = Solution()
print(sol.IsContinuous([0,3,2,6,4]))
print(2/3)
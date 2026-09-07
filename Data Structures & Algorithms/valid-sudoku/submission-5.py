class Solution:
    def isValidStraight(self,line):
            hashtable = {}
            for num in line:
                if num not in hashtable:
                    hashtable[num] = 1
                else:
                    hashtable[num] += 1
            if '.' in hashtable:
                return(len(line) == (len(hashtable)+hashtable["."]-1))
            return(len(line) == len(hashtable))
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.isValidStraight(row):
                return False
        
        for col in zip(*board):
            if not self.isValidStraight(col):
                return False

        r=3
        c=3
        while(True):

            temp = []
            for i in range(r-3, r):
                for j in range(c-3,c):
                    temp.append(board[i][j])

            if not self.isValidStraight(temp):
                return False
                
            if c>=9 and r>=9:
                break
            
            if(r<9):
                r+=3
            else:
                r = 3
                c+=3




        return True
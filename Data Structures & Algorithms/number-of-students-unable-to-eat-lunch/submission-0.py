class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable = len(students)
        for sandwich in sandwiches:
            #print("sandwich:" , sandwich)
            if (sandwich in students):

                for i in range(len(students)):
                    if students[i] == sandwich:
                        #print("index", i)
                        students[i] = 2
                        break                
                unable-=1

            else:
                return unable

        return unable

from Match import Match

class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots
    
    def get_matches(self):

        finalpair=[]
        d1 = {}                      #students: hospitals
        self.hosp_open_slots         #hospitals: positions available

        for i in range(1, self.n + 1):      # d1 key is student = 0
            d1[i] = 0

        count = 0                           # number of positions available total
        for k in self.hosp_open_slots:
            count += self.hosp_open_slots[k]


        print(self.hospital_list)

        i =1
        while count != 0:


            pos = self.hosp_open_slots[i]       #number of pos avail at that hospital
            print(pos)
            print(self.hospital_list[i][0])

            if pos==0:
                if (i==self.m):
                    i=1
                    continue
                else:
                    i+=1
                    continue


            if d1[self.hospital_list[i][0]] == 0:
                d1[self.hospital_list[i][0]] = i
                pos -= 1
                self.hosp_open_slots[i] = pos

                del(self.hospital_list[i][0:1])
                #print("newhospital list")
                #print(self.hospital_list)
                count -= 1
            else:               #student is already paired with hospital
                studentpref = self.student_list[self.hospital_list[i][0]]
                prevhosp = d1[self.hospital_list[i][0]]
                print("prevhosp")
                print(prevhosp)
                indexprevhosp = studentpref.index(prevhosp)
                print("INDEXprevhosp")
                print(indexprevhosp)
                indexcurrhosp = studentpref.index(i)
                print("INDEXcurrent")
                print(indexcurrhosp)

                if indexprevhosp < indexcurrhosp:           #do nothing
                    del(self.hospital_list[i][0:1])
                else:                                       # UPDATE
                    self.hosp_open_slots[prevhosp] += 1
                    d1[self.hospital_list[i][0]] = i

                    pos -= 1
                    self.hosp_open_slots[i] = pos
                    del (self.hospital_list[i][0:1])
                    print(d1)
                    print(self.hosp_open_slots)



            if i == self.m:
                i = 1

            else:
                i += 1

        for key in d1:
            if d1[key]!=0:
                pair=(d1[key],key)
                finalpair.append(pair)


        '''count =5;
        a=1

        while count!=0:
            print(count)
            if a==1:
                print("hey")
                continue

            count-=1; '''

        return finalpair


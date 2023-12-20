class Student:
    def __init__(self):
        pass
    def inputs(self,num,name,score):
        self.number = num
        self.name = name
        self.a = int(score[0])
        self.b = int(score[1])
        self.c =  int(score[2])

    def print_stident(self):
        print("{},{},{},{},{}".format(self.number,self.name,self.a,self.b,self.c))

l=[]
n = int(input())
for i in range(n):
    st = Student()
    s = list(input().split())
    score = s[2:]
    st.inputs(s[0], s[1], score)
    l.append(st)

def printaver(index):
    num=0
    for i in l:
        num+=l[i].score[n]
    print(num/len(l))

printaver(0)
q1=""" is python case sensitive when dealing with identifiers?
   a.yes
   b.no
   c.machine dependent
   d.none """
q2=""" which of the following not a keyword?
   a.eval
   b.assert
   c.local
   d.pass """
q3=""" which one of the floor division?
   a=/
   b=//
   c=%
   d=none """
q4=""" what is the output of the 3*1**3?
   a=27
   b=9
   c=3
   d=none """
q5=""" "a"+"bc"=??
   a=a
   b=bc
   c=abc
   d=none """

questions={q1:"a",q2:"a",q3:"b",q4:"c",q5:"c"}

name=input("enter your name:")
print("hello",name,"welcome to my world")
score=0
for i in questions:
    print(i)
    flag1=input('Do you want to skip the question (yes/no):')
    if flag1=="yes":
        continue
    ans=input("enter your answer (a/b/c/d):")
    if ans==questions[i]:
        print("correct answer,you got 1 point")
        score+=1
        print("correct score :",score)
    else:
        print("wrong answer, you lost 1 point")
        score-=1
        print('corrent score is:',score)
    flag2=input('Do you wnat to quit the quize (yes/no):')
    if flag2=='yes':
        break
print("final score:",score)    


q1="""1.what is the capital of bangladesh?
a.dhaka
b.india
c.canada
d.srilanka
"""
q2="""2.which one of them is float division:
a./
b.//
c.%
d.none
"""
q3="""3.which one of them is not keyword:
a.eval
b.assert
c.local
d.pass
"""
q4="""4.Python is a?:
a.Snake
b.Programming Language
"""
q5="""5.Which of the following is not a stable sorting algorithm?
a) Insertion sort
b) Selection sort
c) Bubble sort
d) Merge sort
"""
q6="""6."a"+"bc"?
a) a
b) bc
c) bca
d) abc
"""
q7="""7."abcd"[2:]?
a) a
b) bc
c) bca
d) abc
"""
q8="""8.What arithmetic operators cannot be used with strings?
a) +
b) *
c) –
d) All of the mentioned
"""

question={q1:'a',q2:'a',q3:'b',
          q4:'b',q5:'b',q6:'d',q7:'c',
          q8:'c'}

print(f'{"Learn Python":=^50}')
name=input('enter your name:')
id=input('enter your id:')
print('your name is:'+name+", ",end='')
print('your id:'+id+'.')
print()

score=0

for x in question:
    print()
    print(x)
    flag=input('Do you want skip the question(y/n):')
    if flag=='y'or flag=='Y':
        continue
    ans=input('select any one a/b/c/d:')
    if ans==question[x]:
        print('Correct!,you get 1 point.')
        score=score+1
        print('your score:',score)
    else:
        print('Wrong!,you get negative mark 1.')
        score=score-1
        print('score is:',score)
    flag2=input('Do you want quit(y/n):')
    if flag2=='y'or flag2=='Y':
        break
print()
if score>2:
    print('Congratulations! you pass in the exam.')
    print('Your total score:', score)
else:
    print('Sorry! you Fail in the exam.')
    print('Your total score:', score)



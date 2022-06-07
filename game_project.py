#opening the file uploaded and getting a random word 
import random
x=open('wordlist_for word game.txt').read() 
a=x.split()
while True:
    word=(random.choice(a)).lower()
    if len(word)>=4:
        break
print('word size is',(len(word)*'*'))


print('number of guesses to guess the word is 16')
turns=16
k=len(word)
l=[]
for i in range(k):
    l.append('*')


while turns>0:
    print('Total guesses u have is',turns)
    b=input('Guess the word :')
    z=0
    for i in word:
        if b==i:
            l[z]=i
        z=z+1
    
    for i in range(len(l)):
      print(l[i])
    if b  in list(word):
      print('your guess is correct')
    else: print("your guess is wrong")
    if(l==list(word)): break
    turns=turns-1


if(turns>0):
    print("you won and the word is",word)
else: print("you lost,Better luck next time",word)
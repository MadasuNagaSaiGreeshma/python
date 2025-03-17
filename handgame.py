a=str(input())
b=str(input())
if(a==rock and b==paper):
   print("paper")
elif(a==scissor and b==paper):
   print("scissor")
elif(a==rock and b==scissor):
    print("rock")
else:
   print("tie")

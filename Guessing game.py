import random as ran
ctr=0
ans="y"
while ans=="y":
    a=ran.randint(10,50)
    for i in range(5):
      guess=int(input("Guess a number in range 10 to 50:"))
      if guess==a:
         print("YOU WIN!!!:)")
         break
      elif guess>a:
         print("Guessed number is greater than actual number")
      elif guess<a:
         print("Guessed number is less than actual number")
      else:
         ctr=ctr+1
    else:
         print("YOU LOSE:(\n The number was",a)
      
    ans=input("Do you want to play again(y or n):")
    if ans!="y":
          print("thank you for playing")

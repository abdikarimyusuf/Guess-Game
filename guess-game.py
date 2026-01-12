import random

ran_1=random.randint(1,100)
while True:
 try:

  user=input("guess num 1-100:")
  guess =int(user)

  



  if guess < ran_1:
   print ("too low")
  elif guess > ran_1:

   print ("too high")
  else:
   print ("well done ")
   break
 except:
  print ("input a number")

# just practicing 
    
    



 

     


  
  






name = input("enter your name:")
yourscore = 0
compscore = 0
def rolldice():
  import random
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print("computer rolled", dice1)
  print(name + " rolled", dice2)

rolldice()








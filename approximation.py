import os
import time

os.system("cls")
print(f"""Welcome to the best Square Root Solver of the world
 """)

start = time.time()

goal = int(input("""Write a integer number: 
"""))

#//Epsilon means how accurate we want to be the approximity of the 
#//calcualtion of the square root

epsilon = 0.01

#//Step help us to define of big or small want our step 

step = epsilon ** 2

#//We gonna use answer to count every possibility of the answer

answer = 0.0

#//interactions counts how many interactions did the while loop to 
#//get an approximate answer

interactions = 0



#//This while loop first subtract we gave it from input answer (goal)
#//with the answer squared, at the star the variable (answer) will be 
#//0.0 and then we are going to add a (step = 0.001) to the variable 
#//answer and then the while loop will run again but this time 
#//answer will be worth of 0.0001 and then 0.0002 and then 0.0003
#//and so on

while abs(answer**2 - goal) >= epsilon and answer <= goal:

    interactions += 1

    answer += step

#    print(abs(answer))

end = time.time()
tiempo = round(end-start,3)


if abs(answer ** 2 - goal) >= epsilon:
    
    print(f"""In {tiempo} seconds we approach the answer and we find: 
""")
    print(f"""Not fount square root of {goal} but did {interactions} interactions
""")
else:

    print(f"""In {end-start} seconds we approach the answer and we find: 
""")
    print(f"""The square root of {goal} is {answer} and did {interactions} interactions
""")
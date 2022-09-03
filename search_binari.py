import os


def main():
    os.system("cls")

    try:

        #Welcome to the program

        print(f"""Welcome to the best Square Root Solver of the world
        """)


        choice_between_methods = int(input("""But we need to you select a method to resolve it
Press 1 to use the method proximity or press 2 to use the method binary search: """))

        #if you write a number that is not 1 or 2 is gonna pop out a assert alert saying "invalid answer"

        assert choice_between_methods > 0 and choice_between_methods < 3, "invalid answer"

        #and and we print it
        
        print(f"Ok, you pressed {choice_between_methods}")


        #now depend on what number do you wrote will chosse the method 1 or method 2

        if choice_between_methods == 1:

            #This one is the approximation
            metodo_1()

        elif choice_between_methods == 2:

            #This one is the search binari
            metodo_2()

    
    except AssertionError:
        print("Try again and choose a number between 1 or 2")


#///////////////////////////////////////////////////////////


def metodo_1():
    
    #goal will the number that we want to find his square root

    goal = int(input("Choose a interal number: "))

    #epsilon is how presice do we want it to be

    epsilon = 0.01
    
    #step means the amount of decimals we want to add on each interactions

    step = epsilon ** 2

    #the answer will count the aproximation for every interaction

    answer = 0.0


    #This while loop first subtract we gave it from input answer (goal)
    #with the answer squared, at the star the variable (answer) will be 
    #0.0 and then we are going to add a (step = 0.001) to the variable 
    #answer and then the while loop will run again but this time 
    #answer will be worth of 0.0001 and then 0.0002 and then 0.0003
    #and so on


    while abs(answer**2 - goal) >= epsilon and answer <= goal:

        answer += step
    #optional         print(answer)

    if abs(answer ** 2 - goal) >= epsilon:
        print(f"Not fount square root of {goal}")
    else:
        answer = round(answer,3)
        print(f"The square root of {goal} is {answer}")

#///////////////////////////////////////////////////////////

def metodo_2():

    #goal will the number that we want to find his square root

    goal_2 = int(input("Write a number: "))

    #epsilon is how presice do we want it to be

    epsilon_2 = 0.01

    #down is goin to be the lowest point of the data

    down = 0.0

    #up is integer that represents the lowest point and the highest (goal_2)

    up= max(1.0,goal_2)

    #answer is gonna represent the mniddle of the max (or highest) point of the goal_2

    answer_2 = ( up + down ) / 2


    while abs (answer_2 **2 - goal_2) >= epsilon_2:
        print(f"up = {up} down = {down} ,answer = {answer_2}")
        if answer_2 **2 < goal_2:
            down = answer_2
        else:
            up = answer_2

        answer_2 = (up + down) / 2
        answer_2 = round(answer_2,3)

    print(f"The square root of {goal_2} is {answer_2}")



if __name__ == '__main__':
    main()

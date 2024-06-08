'''Q: Write a code for the reeborg to complete the hurdles infront of him and reached the goal'''

#link for the game page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

### Write your code below

#NOTES: In Reeborg site we have default functions move() and turn_left() and at_goal()



# Solution_Code
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# Method_1
while at_goal != True:
    jump()

# Method_2
while at_goal() == False:
    jump()

#Method_3:
while not at_goal():
    jump()


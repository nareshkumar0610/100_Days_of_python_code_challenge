'''Q: Write a code for the reeborg to complete the hurdles infront of him'''

#link for the game page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

### Write your code below

#NOTES: In Reeborg site we have default functions move() and turn_left()



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
    
for i in range(1, 7):
    jump()

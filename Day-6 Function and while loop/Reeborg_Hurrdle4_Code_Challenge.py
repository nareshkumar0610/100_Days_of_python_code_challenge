'''Q: Write a code for the reeborg to complete the hurdles and reached the goal'''

#link for the game page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

### Write your code below

#NOTES: In Reeborg site we have default functions move(), turn_left(), wall_in_front(), front_is_clear(), wall_on_right() and at_goal()



# Solution_Code
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()
    
while at_goal() != True:
    if wall_in_front() == True:
        jump()        
    else:
        move()
        

        
    
    

import random

def rotate(id):    # this function is used whenever the user must rotate the arm
    color = get_container(id)[str(id)+'1']
    old_reading = potentiometer.right()    # pre-define value for old_reading
    
    while not arm.check_autoclave(color):   # allows the user to rotate the potentiometer until the correct autocalve is reached
        new_reading = potentiometer.right()     
        delta = new_reading - old_reading     
        angle = delta*348               # this allows for the arm to be rotated in increments simulating a smooth rotation
        arm.rotate_base(angle)
        time.sleep(0.2)    # sleep is used here to allow the arm to move before changing the value of the readings
        old_reading = new_reading 

def pickup(id):   # this function is used to pickup the block once spawned
    arm.home()  # not necessary but impleneted for caution
    time.sleep(1)
    arm.move_arm(0.586, 0.021, -0.068)     # moves the arm to the exact spawn location for the containers
    time.sleep(1)
    if id<4:        # compares the ID to check if container is small or not
        arm.control_gripper(35)     # if small, the gripper closes slightly more so it can pick up the smaller container
    else:
        arm.control_gripper(30)     # if big, it'll close slightly less relatively as to not crush the container
    
    time.sleep(1)
    arm.move_arm(0.406,0.0,0.483)   # moves arm to the home position / did not use arm.home() as it opens the gripper
    time.sleep(1)
     
def spawn_cage(list_container):     # simply spawns a container then subsequently removes that ID from the list of containers as to not spawn the same container twice
     arm.spawn_cage(list_container[0])
     list_container.pop(0)  
     
     return list_container
     
def get_container(id):      # this function returns a dictionary that contains 2 values for the containers color and size
                    
    id = int(id)  # to convert the ID from a string to integer so they can go through in the 'if' statements
    
    if id==1 or id==4:
        color = 'red'
            
    elif id==2 or id==5:
        color = 'green'
            
    elif id==3 or id==6:
        color = 'blue'
                    # 'if' statements to attain a containers color and shape
    if id<4:
        size = 'small'
    else:
        size = 'large'
    
    container = {str(id)+'1':color,str(id)+'2':size} 
    # EXAMPLE: if the containers ID = 1, the colors value in the dict would be 11 and size would be 12
    return container

def dropoff(id):      # function to dropoff the container
    item_dropped = False
    color = get_container(id)[str(id)+'1']  # use get_container to get the shape and size for the container
    size = get_container(id)[str(id)+'2']
    containerdrop = {'3': [-0.613, 0.222, 0.302], '6': [-0.436, 0.158, 0.165], '1': [-0.005, -0.617, 0.300],
                     '4': [-0.004, -0.415, 0.172], '2':[-0.005, 0.605, 0.275],'5':[-0.004, 0.442, 0.172]}
        # the above dictionary containers the container IDs with their respective dropoff coordinates contained in a list where X is [0], Y is [1], and Z is [2]
    drop = containerdrop[str(id)]      
    if id<4:    # separate if statements for whether the container is big or small
        print('Move the left potentiometer to 60 to drop the',color,'container into the',size,'autoclave.') # print statement for ease of use for the user
        while not item_dropped: # while loop to wait for an input by the user
                if potentiometer.left()==0.6:
                    print('Dropping off...')
                    time.sleep(1)    
                    arm.move_arm(drop[0],drop[1],drop[2])   # moves arm to the respective container dropoff location
                    time.sleep(1)
                    arm.control_gripper(-35)   # opens gripper to drop container
                    time.sleep(1)
                    arm.home()      # takes arm back to home location
                    time.sleep(2)
                    arm.deactivate_autoclaves()     
                    time.sleep(1)
                    print('Dropoff complete!')
                    item_dropped = True # if statement runs once then ends, completing the system
    else:
        print('Move the left potentiometer to 100 to drop the',color,'container into the',size,'autoclave.')
        while not item_dropped:     # while loop to wait for an input by the user
                if potentiometer.left()==1.0:
                    arm.open_autoclave(color)     # opens the autoclave as container is big
                    print('Dropping off...')
                    time.sleep(2)    
                    arm.move_arm(drop[0],drop[1],drop[2])   # moves arm to the respective container dropoff location
                    time.sleep(2)
                    arm.control_gripper(-30)     # opens gripper to drop container
                    time.sleep(2)
                    arm.home()
                    time.sleep(2)
                    arm.open_autoclave(color,False)     # closes the container
                    time.sleep(1)
                    arm.open_autoclave(color,False)     # 2 times as autoclave sometimes would not close
                    time.sleep(1)
                    arm.deactivate_autoclaves()
                    time.sleep(1)
                    print('Dropoff complete!')
                    item_dropped = True
                    
    

    
def main():    # main function which will be the input to run the whole code
    run = 0   # predefined variable to display which run it is on
    list_container = [1,2,3,4,5,6]  # container IDs
    random.shuffle(list_container)  # shuffles the containers   
    
    while run<6:    # while loop to iterate 6 times
        run+=1  # adds 1 to the run value each time the program runs
        
        arm.activate_autoclaves()   
        id = list_container[0]  # takes a random value from the container IDs
        list_container = spawn_cage(list_container)  # spawns a container and removes that ID from the list as to not repeat the same container

        color = get_container(id)[str(id)+'1']
        size = get_container(id)[str(id)+'2']
        
        pickup(id)      # pickup the container

        print('Picking up...')    
        
        print('Container ID',id,'was spawned. Use the right potentiometer to move arm to the',color,'autoclave.')
        
        rotate(id)      # allows user to move the potentiometer to control the arm
        
        print('Arm has been moved to the right spot!')
        
        dropoff(id)     # drops off the container once the container has been moved to the right location
                    
        print('Move both potentiometers to 50 in order to continue.')
       
        parameter = False   
        
        while not parameter:  # while loop to wait for the user to set both potentiometers to 50 before running the program again
            if potentiometer.right()==0.5 and potentiometer.left()==0.5:
                parameter = True
    
    print('All containers have been transferred.\nProgram terminated.')   # once program has run 6 times, program tells the user that it was terminated and all containers were transferred
    
    

def rotate():    
    old_reading = potentiometer.right()
    left_value = potentiometer.left()
    
    while left_value != 1.0 :   
        new_reading = potentiometer.right()     
        delta = new_reading - old_reading     
        angle = delta*348               
        arm.rotate_base(angle)
        time.sleep(0.2)    
        old_reading = new_reading 

def pickup():   
    arm.home()  
    time.sleep(1)
    arm.move_arm(0.486, 0.0, 0.109)     
    time.sleep(1)       
    arm.control_gripper(27)     
                                
    time.sleep(1)
    time.sleep(1)
     

def small_dropoff(id):     
    item_dropped = False
    containerdrop = {'1': [-0.005, -0.617, 0.300],'2': [0,0,0]}            
       
    drop = containerdrop[str(id)]      
    if id<4:    
        while not item_dropped: 
                if potentiometer.left()==0.6:
                    print('Dropping off...')
                    time.sleep(1)    
                    arm.move_arm(drop[0],drop[1],drop[2])   
                    time.sleep(1)
                    arm.control_gripper(-35)   
                    time.sleep(1)
                    arm.home()      
                    time.sleep(2)
                    arm.deactivate_autoclaves()     
                    time.sleep(1)
                    print('Dropoff complete!')
                    item_dropped = True 
    else:
        while not item_dropped:    
                if potentiometer.left()==1.0:
                    arm.open_autoclave(color)   
                    print('Dropping off...')
                    time.sleep(2)    
                    arm.move_arm(drop[0],drop[1],drop[2]) 
                    time.sleep(2)
                    arm.control_gripper(-30)
                    time.sleep(2)
                    arm.home()
                    time.sleep(2)
                    arm.open_autoclave(color,False) 
                    time.sleep(1)
                    arm.deactivate_autoclaves()
                    time.sleep(1)
                    print('Dropoff complete!')
                    item_dropped = True
                    
    
def main():    
    run = 0    
    
    while run<2: 
        run+=1  
        
        arm.activate_autoclaves()   

        color = get_container(id)[str(id)+'1']
        size = get_container(id)[str(id)+'2']
        
        pickup(id)     

        #print('Picking up...')    
        
        #print('Container ID',id,'was spawned. Use the right potentiometer to move arm to the',color,'autoclave.')
        
        rotate(id)      
        
        #print('Arm has been moved to the right spot!')
        if run==0:
            dropoff1(id)
        if run==1:
            dropoff2(id)     
                    
        #print('Move both potentiometers to 50 in order to continue.')
       
        parameter = False   
        
        while not parameter:  
            if potentiometer.right()==0.5 and potentiometer.left()==0.5:
                parameter = True
    
    print('All containers have been transferred.\nProgram terminated.')   
    
    
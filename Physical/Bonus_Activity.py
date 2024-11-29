def pickup():  
    arm.home()  
    time.sleep(1)
    arm.move_arm(0.621,-0.065,0.109)   
    time.sleep(1)       
    arm.control_gripper(40)              
    time.sleep(1)
    arm.move_arm(0.406,0.0,0.483) #home 
    time.sleep(3)
    
def rotate_base():
    old_reading = potentiometer.right()
    item_dropped = False
    
    while not item_dropped:   
        new_reading = potentiometer.right()     
        delta = new_reading - old_reading     
        angle = delta*348               
        arm.rotate_base(angle)
        time.sleep(0.2)    
        old_reading = new_reading 
        if potentiometer.left()>=0.5:
            item_dropped = True
            break
    time.sleep(3)
    
def drop_off():
    item_dropped = False
    while not item_dropped:
        time.sleep(2)    
        arm.move_arm(0.007,-0.395,0.244)   #autoclave
        arm.control_gripper(-27)   
        time.sleep(1)
        arm.home()      
        time.sleep(2)
        item_dropped=True
        
        

def main():
    
    arm.activate_autoclaves()
    
    item_dropped = False
    autoclave_open = False
    while not item_dropped:
        while not autoclave_open:
            if potentiometer.left()>=0.5:
                arm.open_autoclave('red')
                autoclave_open = True
                
        pickup()
        
        rotate_base()
        
        drop_off()
        
        while autoclave_open:
            if potentiometer.left()<=0.5:
                arm.open_autoclave('red',False)
                autoclave_open = False
                
        time.sleep(8)
        
        item_dropped = True
        
    arm.deactivate_autoclaves()
        
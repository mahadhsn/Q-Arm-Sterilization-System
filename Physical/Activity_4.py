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
    arm.move_arm(-0.2,-0.448,0.252) 
    arm.control_gripper(-40)   
    time.sleep(1)
    arm.home()      
    time.sleep(3)

def main():
    
    item_dropped = False
    
    while not item_dropped:
        
        arm.activate_autoclaves()
        
        pickup()
        
        rotate_base()
        
        drop_off()
        
        arm.deactivate_autoclaves() 
        
        item_dropped = True
        
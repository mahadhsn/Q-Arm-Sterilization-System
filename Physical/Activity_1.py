def pickup():  
    arm.home()  
    time.sleep(1)
    arm.move_arm(0.621,-0.065,0.109)     
    time.sleep(1)       
    arm.control_gripper(40)              
    time.sleep(1)
    arm.move_arm(0.406,0.0,0.483) #home
    time.sleep(3)
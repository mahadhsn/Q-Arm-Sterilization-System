def drop_off():
    arm.activate_autoclaves()
    time.sleep(2)    
    arm.move_arm(-0.2,-0.448,0.252)    #autoclave
    arm.control_gripper(-40)   
    time.sleep(1)
    arm.home()      
    time.sleep(2)
    arm.deactivate_autoclaves()     
    time.sleep(3)
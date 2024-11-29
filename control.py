def control():
    arm.activate_autoclaves()
    item_dropped=False
    x=0
    old_reading=potentiometer.right()
    while not item_dropped:
        
        if potentiometer.left() == 0.0:
            new_reading = potentiometer.right()
            delta = new_reading - old_reading
            angle = delta*348
            arm.rotate_base(angle)
            time.sleep(0.2)
            old_reading = new_reading
            if arm.check_autoclave('red'):
                arm.open_autoclave('red')
            elif not arm.check_autoclave('red'):
                arm.open_autoclave('red',False)  
                 
            if arm.check_autoclave('blue'):
                arm.open_autoclave('blue')    
            elif not arm.check_autoclave('blue'):
                arm.open_autoclave('blue',False)
            
            if arm.check_autoclave('green'):
                arm.open_autoclave('green')    
            elif not arm.check_autoclave('green'):
                arm.open_autoclave('green',False)
        
        elif potentiometer.left() == 0.3:
            new_reading = potentiometer.right()
            delta = new_reading - old_reading
            angle = delta*348
            arm.rotate_shoulder(angle)
            time.sleep(0.2)
            old_reading = new_reading        
                        
        
        elif potentiometer.left() == 0.5:
            new_reading = potentiometer.right()
            delta = new_reading - old_reading
            angle = delta*150
            arm.rotate_elbow(angle)
            time.sleep(0.2)
            old_reading = new_reading
            
        elif potentiometer.left() == 0.7:
            new_reading = potentiometer.right()
            delta = new_reading - old_reading
            angle = delta*60
            arm.control_gripper(angle)
            time.sleep(0.2)
            old_reading = new_reading
        
        elif potentiometer.left() == 1.0:
            if x<6:
                x+=1
                arm.spawn_cage(x)
            else:
                item_dropped=True
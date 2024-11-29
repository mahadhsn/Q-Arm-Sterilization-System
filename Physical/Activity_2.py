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
import time
import os
#import winsound
for h in range(1, 24):
    for m in range(1, 60):
        for s in range(1, 60):
            print("h: ", h, "m: ", m, "s: ", s)
            time.sleep(1)
            os.system("cls")
            frequency = 2000  # Set Frequency To 2500 Hertz
            duration = 5000  # Set Duration To 1000 ms == 1 second
            def playsound(frequency,duration):
            #apt-get install beep
                os.system('beep -f %s -l %s' % (frequency,duration))
           # os.system('beep -f %s -l %s' % (frequency,duration))
            
           # winsound.Beep(frequency, duration)


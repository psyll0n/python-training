#! python3
<<<<<<< HEAD
# multihreadDemo.py - Multi-threading example.
=======
# multihreadDemo.py - Multi-threading example. 
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c

import threading, time


<<<<<<< HEAD
print("Start of program.")
=======
print('Start of program.')
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c


def takeANap():
    time.sleep(5)
<<<<<<< HEAD
    print("Wake up!")

=======
    print('Wake up!')
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c

threadObj = threading.Thread(target=takeANap)
threadObj.start()


<<<<<<< HEAD
print("End of program.")
=======
print('End of program.')


>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c

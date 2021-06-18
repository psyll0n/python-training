#! python3
<<<<<<< HEAD
# multihreadDemo.py - Multi-threading example.
=======
<<<<<<< HEAD
# multihreadDemo.py - Multi-threading example.
=======
# multihreadDemo.py - Multi-threading example. 
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c
>>>>>>> 51f83aa0df79342ce37a1dae69bfcd0ce4286810

import threading, time


<<<<<<< HEAD
print("Start of program.")
=======
<<<<<<< HEAD
print("Start of program.")
=======
print('Start of program.')
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c
>>>>>>> 51f83aa0df79342ce37a1dae69bfcd0ce4286810


def takeANap():
    time.sleep(5)
<<<<<<< HEAD
    print("Wake up!")

=======
<<<<<<< HEAD
    print("Wake up!")

=======
    print('Wake up!')
>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c
>>>>>>> 51f83aa0df79342ce37a1dae69bfcd0ce4286810

threadObj = threading.Thread(target=takeANap)
threadObj.start()


<<<<<<< HEAD
print("End of program.")
=======
<<<<<<< HEAD
print("End of program.")
=======
print('End of program.')


>>>>>>> 2d31c822d90260ba29f5b99f048854f90daccf4c
>>>>>>> 51f83aa0df79342ce37a1dae69bfcd0ce4286810

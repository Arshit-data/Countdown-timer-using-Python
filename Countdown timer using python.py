#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

def countdown(t):
    try:
        t = int(t)
    except ValueError:
        print("Invalid input, please enter a valid integer")
        return

    if t <= 0:
        print("Please enter a positive value for the countdown timer")
        return

    while t > 0:
        minutes, seconds = divmod(t, 60)
        timeformat = "{:02d}:{:02d}".format(minutes, seconds)
        print(timeformat, end="\r")
        time.sleep(1)
        t -= 1

    print("Fire in the Hole")

user_input = input("Enter the countdown in seconds: ")

countdown(user_input)


# In[ ]:





# In[ ]:





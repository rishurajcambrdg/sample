
### Take a break ia a simple IDLE program which gives you the ability to take short breaks during your work hours.
### Although not being a gui app , it aims to teach beginners learn how to slwwp your programs and functionality to open web browsers.


import webbrowser
import time

c = input("Please enter the number of times you want a break: ")
t = input("How many minute long sessions do you want: ")

count = 0
print("This program started om" + time.ctime())
while(count < c):
    time.sleep(t*60)
    webbrowser.open("http://www.youtube.com.")
    print("the time is" + time.ctime())
    count += 1

    
  

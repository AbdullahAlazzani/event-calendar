"""/ Abdullah Alazzani
This project is a simple calender that you can add event to it
"""
from time import sleep, strftime

user_fist_name = ("Alazzani")
calendar = {}
def welcome():
  print (""" Hello 
  Welcome to Azzon calendar 
  I hope you will enjoy it ^_^""")
  sleep(1)
  print ("Today is: " + strftime("%A %B %d, %Y"))
  print ("The time is: " + strftime("%H:%M:%S"))
  print ("What would you like to do?")
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ").upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print ("Calendar is empty.")
      else:
        print (calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print (" The update being suceeful")
      print (calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print ("Sorry, invalid date was entered.")
        try_again = raw_input("Try Again? Enter Y for yes, N for No: ").upper
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print ("Calendar is empty")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print ("The event was Successfully feleted.")
          else:
            print ("Sorry, incorrect event was specified")
    elif user_choice == "X":
          start = False
    else:
          print ("Sorry, invalid command was entered.")
          sleep(2)
          start = False
            
start_calendar()  

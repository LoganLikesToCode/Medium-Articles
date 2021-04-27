import calendar

def cal(year):
  opt = input("Would you like the schedule of the year? y/n: ")
  
  if opt == "y":
    print(calendar.calendar(year))
   
  if opt == "n":
    print("Alright!")
  
year = int(input("What year: "))
final_year = year / 4
final_bool = final_year.is_integer()

if final_bool == True:
  print("This year is a leap year!")
  cal(year)
 
elif final_bool != True:
  print("This year is not a leap year!")
  cal(year)

## imports what you have
from urllib.request import urlopen 

def get_condition(city):
  url = "http://wttr.in/" + city + "?format=%C"
  page = urlopen(url)
  raw = page.read()
  condition = raw.decode("utf-8")
  return condition
#this block defines the condition of getting a city then returns the information

#a simple input
city = input("City: ")
#redefining condition? or just making def get_condition(city) another variable
condition = get_condition(city)
# if statement
if condition == "clear":
  print("no umbrella needed")
else:
    print("Bring an Umbrella")
import sys
locations = sys.path
# print(locations) This will print the list of directories where Python looks for modules and was not visually appealing
# for location in locations:
#     print(location)
# This will print the list of directories where Python looks for modules and was visually appealing
# Now with list comprehension
# print([location for location in locations]) # This printed a list of directories where Python looks for modules
# [print(location) for location in locations] # This printed the directories where Python looks for modules.  Look at the difference between the two print statements


import calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitaleapyear = calendar.isleap(2036)
print(isitaleapyear)
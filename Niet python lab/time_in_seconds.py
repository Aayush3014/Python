#Convert Time into seconds
#sec=hours*3600+minutes*60

hours = int(input("Enter Time in hours : "))
minutes = int(input("Enter Time in minutes : "))

seconds = hours * 3600 + minutes * 60

print(f'Time in seconds : {seconds}')

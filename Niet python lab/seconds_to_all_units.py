# Python program to convert seconds into day, hour, minutes, and seconds

time = float(input("Enter time n seconds : "))
day = time//(24 * 3600)
time = time % (24 * 3600)
hours = time//3600
time %= 3600
minutes = time//60
time %= 60
seconds = time

print(f'{day} days {hours} hours {minutes} minutes {seconds} seconds')

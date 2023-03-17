mintues = (seconds - hours * 3600) //60
remaining_seconds = seconds - hours * 3600 - mintues * 60
return hours, mintues, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
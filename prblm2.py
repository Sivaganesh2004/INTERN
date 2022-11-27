//calculate days in a month and year
month=int(input("ENTER THE MONTH:"))
year=int(input("ENTER THE YEAR:"))

if((month==2) and (year%4==0) or (year%400==0)):
	print("NUMBER OF DAYS IS 29");
elif(month==2):
	print("NUMBER OF DAYS IS 28");
elif(month==1 or  month==3 or month==5 or month==7 or  month==8 or month==10 or month==12):
	print("NUMBER OF DAYS IS 31");
else:
   print("NUMBER OF DAYS IS 30");

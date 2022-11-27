str1=(input("ENTER THE STRING:"))
n=str(str1)[::-1]
print(n)
if(str1==str1[::-1]):
	print("IT IS A PALINDROME..")
else:
   print("IT IS NOT A PALINDROME..")
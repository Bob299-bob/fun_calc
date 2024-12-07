name = input('Enter your Name \n: ')
print("Hello " + name, " \n ThIS IS OUR FUN SHOP")
print('I AM MANAGER HERE, \n FIRST WE CHECK HOW OLD ARE YOU ! ')
s1 = input('ENTER YOUR BIRTH YEAR \n: ')
age = 2024 - int(s1)
print('Yeah We Got It Dear '+name, 'Your Current Age Is ')
print(age)
print('So Dear '+name, '\n How Can I Entertain You \n  ...... \n should we play calculator tricks !! ')
s2=input('Please press ENTER to start: ')
print("Here is your calculator")
print("So What Operation Will You Perform \n Here Is A List \n1. Addition \n2. Substraction \n3. Multiplication \n4. Divide \n5. Percentage")
s3 = input('Please Select One Operation . ')
if(int(s3)==1):
     a=input('Enter 1st no. ')
     b=input('Enter 2nd no. ')
     c=int(a)+int(b)
     print("Your Addition is: ")
     print(int(c))
     print("All The Best " +name)
elif(int(s3)==2):
     a=input('Enter 1st no. ')
     b=input('Enter 2nd no. ')
     c=int(a)-int(b)
     print("Your substraction is: ")
     print(int(c))
     print("All The Best " +name)
elif(int(s3)==3):
     a=input('Enter 1st no. ')
     b=input('Enter 2nd no. ')
     c=int(a)*int(b)
     print("Your Multiplication is: ")
     print(int(c))
     print("All The Best " +name)
elif(int(s3)==4):
     a=input('Enter 1st no. ')
     b=input('Enter 2nd no. ')
     c=float(a)/float(b)
     print("Your Result is: ")
     print(float(c))
     print("All The Best " +name)
elif(int(s3)==5):
     a=input('Enter Total value ')
     b=input(' At what value you want percentage ')
     c=float(b)*100/float(a)
     print("Your Percent Value is: ")
     print(float(c),'%')
     print("All The Best " +name)
elif(int(s3)==6):
     a=input("ff")
     b=input(" d")
     while(int(a)<10):
          int (a)==int (a)/12+1
          a += b
     print(a)
else:
    print("THANKYOU " +name)


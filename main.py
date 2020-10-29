from time import sleep as sl

    
print("welcome to the demo textbased survival game. what's your name?")
name = input()

print("hello " + name) 
sl(1)

print("the year is 1949, you are stuck in a gulag somewhere in eastern siberia, the current temperature is -35C. you find yourself behind the back of a guard.")
sl(4)

print("do you attack the guard, "+ name +"? enter 'yes' or 'no'")
choice = input()

if choice == 'yes': 
  sl(2)
  print('the guard whips out an AN-94 Nikonov Assault Rifle and shoots you to death.') 
  sl(0.5)
  print("you died")
elif choice == 'no': 
  sl(2)
  print("you survive for 9 more months until april 1950, at which point you are placed onto an electric chair for committing the crime of stealing a potato. ")
  sl(0.5)
  print("you died")
else:
  print("bruh moment imagine not typing in yes or no")


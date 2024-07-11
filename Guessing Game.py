from random import randint
answer = randint(1,10)

while True:
        try:
                guess = int(input ("guess a number from 1 to 10: "))
                if  (guess) > 0 and int (guess) < 11:
                        if (guess) == answer:
                               print("You are genius 😄")
                               break
                else:
                      print("hey bozo 😠,I said 1 to 10 🤣")
        except Exception as ValueError:
         print("please enter a number")
         continue
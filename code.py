low = 0
high = 100
ans = (high + low)/2
print("Please think of a number between 0 and 100.")
while high - low != 0:
    print("Is your secret number " + str(ans) + "?")
    print("Enter 'h' to indiciate that the guess is too high. ", end='')
    print("Enter 'l' to indicate that the guess is too low. ", end='')
    print("Enter 'c' to indicate that I guessed correctly. ", end='')
    ind = input()
    if ind == 'h':
        high = ans
        ans = int((high + low)/2)
    elif ind == 'l':
        low = ans
        ans = int((high + low)/2)
    elif ind == 'c':
        break
    else:
        print("Invalid entry. Please try again.")
print("Game over. Your secret number was: " + str(ans))   
    

## CodersA-Ch-3-Exercises.pdf

# Exercise 3.1
# The cover price of a book is $24.95, but bookstores get a 40 percent discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. Calculate the total wholesale costs for 60 copies.

def wholeSaleCost(coverPrice, percentDiscount, copies, firstShippingCost, addtlShippingCost):
  # finds each book's cost for bookstore, excluding shipping
  bookStoreCost = coverPrice * (1 - (percentDiscount / 100))
  # add shipping cost
  if copies <= 1:
    # only add the initial shipping cost
    return "$" + str(firstShippingCost + (bookStoreCost * copies))
  else:
    # add initial & recurring shipping cost
    return "$" + str(firstShippingCost + ((bookStoreCost + addtlShippingCost) * copies))

print(wholeSaleCost(24.95, 40, 60, 3, 0.75))


# Exercise 3.2
# Can you identify and explain the errors in the following lines of code? Correct them.
# exercise0302.py
# print( "A message" ).
# print( "A message ' )
# print( ' A messagef" ' )

# The first line's error is that there is a period after the closing bracket. Move the period into the quote
print("A message")

# The second line uses a quote and apostrophy around the input. Only single quotes or double quotes can be used in a string, so replace both quotes with ' or both quotes with "
print('A message')

# The third line's f-string is placed in the incorrect place, it must be placed before the input and only one type of quotes can be used
print(f"A message")


# Exercise 3.3
# When something is wrong with your code, Python will raise errors. Often these will be “syntax errors” that signal that something is wrong with the form of your
# code (e.g., the code in the previous exercise raised a SyntaxError). There are also “runtime errors,” which signal that your code was in itself formally correct, but that something went
# wrong during the code’s execution. A good example is the ZeroDivisionError, which indicates that you tried to divide a number by zero (which, as you may know, is not allowed).
# Try to make Python raise such a ZeroDivisionError.

# raise ZeroDivisionError
zeroDivError = 2/0


# Exercise 3.4
# Here is another illustrative example of a runtime error. Run the follow code and study the error that it generates. Can you locate the problem?
# exercise0304.py
# print( ((2*3) /4 + (5 -6/7) *8 )
# print( ((12*13) /14 + (15 -16) /17) *18 )

# The problem lies in the first line, there is an extra open bracket that is never closed, right after print. Fix error by removing the extra bracket


# Exercise 3.5
# You look at the clock and see that it is currently 14.00h. You set an alarm to
# go off 535 hours later. At what time will the alarm go off? Write a program that prints the answer. 
# Hint: for the best solution, you will need the modulo operator.

def alarm(currentTime, setHours):
  # subtracts 1 hour from alarm duration and adds 1 hour to current time until the duration is 0
  while setHours > 0:
    # modulo divide current time by 24 at midnight to go to new day
    if currentTime >= 24:
      currentTime = currentTime % 24
    currentTime += 1
    setHours -= 1
  return(currentTime)

# prints answer
print(alarm(14, 535))

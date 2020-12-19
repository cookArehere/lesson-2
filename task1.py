

"""
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”
Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.

"""
task1 = '{:^65}'.format('Task 1')
print(task1)
print()
#1
name = 'Oleg'
day = 'Monday'

method_one = "Good day " +  name + "! " + day + " is a perfect day to learn some python."
print("method_one: " + method_one)

#2
information = {'name': 'Andry', 'day': 'Tuesday'}

method_two = 'Good day {name}! {day} is a perfect day to learn some python.'.format(**information)
print("method_two: " + method_two)

#3
method_three = 'Good day {0}! {1} is a perfect day to learn some python.'.format("Vika", "Wednesday")
print("method_three: " + method_three)
print()

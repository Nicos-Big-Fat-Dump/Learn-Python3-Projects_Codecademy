# Learn-Python3-Projects_Codecademy
My projects from codecademy 
___

## User Input

### How to assign variables with user input.

So far, we’ve covered how to assign variables values directly in a Python file. However, we often want a user of a program to enter new information into the program.

How can we do this? As it turns out, another way to assign a value to a variable is through user input.

While we output a variable’s value using print(), we assign information to a variable using input(). The input() function requires a prompt message, which it will print out for the user before they enter the new information. For example:

```py
likes_snakes = input("Do you like snakes? ")
```

In the example above, the following would occur:

1. The program would print "Do you like snakes? " for the user.
2.The user would enter an answer (e.g., "Yes! I have seven pythons as pets!") and press enter.
3. The variable likes_snakes would be assigned a value of the user’s answer.

Not only can `input()` be used for collecting all sorts of different information from a user, but once you have that information stored as a variable you can use it to simulate interaction:

```
>>> favorite_fruit = input("What is your favorite fruit? ")
What is your favorite fruit? mango

>>> print("Oh cool! I like " + favorite_fruit + " too, but I think my favorite fruit is apple.")
Oh cool! I like mango too, but I think my favorite fruit is apple.
```

These are pretty basic implementations of input(), but as you get more familiar with Python you’ll find more and more interesting scenarios where you will want to interact with your users.

___

## Match Statements in Python

### Learn how to declare and use match-case statements in Python.

Like the if-else statements, we can also use switch statements to build a program’s control flow. In Python, we have match-case statements that implement switch statements.

Let’s discuss switch and match statements, how to define them in a Python program, and when to use match-case statements instead of if-else statements to build control flow in a program.
What is a Switch Statement?

A switch statement is a control flow statement that executes a block of code, among many others, based on the value of a variable or expression.

Functionally, switch-case statements are almost like if-else statements. For example, let’s look at the code from the if statements exercise.

```py
user_name = "Dave"  
if user_name == "Dave":   
    print("Get off my computer Dave!")   
elif user_name == "angela_catlady_87":   
    print("I know it is you, Dave! Go away!")   
elif user_name == "Codecademy":   
    print("Access Granted.")   
else:   
    print("Username not recognized.")  
```

The above code can be written using a switch statement, as shown in the following code. Don’t worry about the syntax. It’s explained in the next section.

```py
user_name = "Dave"  
switch user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  
```

If you run the above code, it will encounter a SyntaxError because Python does not have a switch keyword. Python didn’t have switch statements or any of its implementations until version 3.10.

In Python 3.10, we got match-case statements that implement switch statements and other functionalities. From now on, we will refer to switch-case statements as match-case statements, as defined in Python.
How to Declare a Match Statement in Python?

We use the match, case, and default keywords to define match-case statements in Python. It has the following syntax:

```py
match expression:  
    case value_1:  
        # code to execute when expression equals value_1  
    case value_2:  
        # code to execute when expression equals value_2  
    case value_3:  
        # code to execute when expression equals value_3  
    case value_4:  
        # code to execute when expression equals value_4  
    case value_N:  
        # code to execute when expression equals value_N  
    case default:  
        # code to execute when expression isn't equal to any of the values  
```
In the above code,

* `match` is a keyword that marks the start of the `match` block.
* The expression can be a variable, an arithmetic expression, a Boolean expression, or a Python object like a list, tuple, or string.
* The code inside a case block is executed for a single value of expression. For example, only if expression evaluates to `value_1` will the code inside the case `value_1` block be executed. If expression evaluates to `value_2`, then only the code inside the case `value_2` block will be executed.
* Only one case block is executed in the entire `match` block for any given value of expression. Once a case block is executed, the program’s control flow moves out of the `match` block.
* The default block is always present at the end of the `match` block. If expression matches none of the values in other case blocks, the code inside case default is executed.

Using the above syntax, we can rewrite the code given in the switch-case example as shown below:

```py
user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  
```

If you run the above code, you will get the following output:

`Get off my computer Dave!`

### When to Use Match Statements in Python?

We can use match-case statements for the following use cases:

* Match-case statements can be an efficient alternative to if-elif-else statements. When a variable or expression can take multiple values, and we need to perform a different action for each possible value, we can use match statements.
* A match-case block can be used for other tasks, like structural pattern matching, in addition to replacing if-else blocks. This helps us check for different conditions on Python objects like lists, tuples, and strings.
* Match-case statements are more readable compared to if-elif-else statements. Hence, in cases where we must check for many values that an expression or variable can take, we should use match-case statements.

___


# Python-
### What is Python?
##### *Python is an 
             - high-level programming language
             - interpreted
             - object-oriented.
It was created by Guido Van Rossum, and released in 1991.
### Why you should learn python?
##### * You should learn Python because 
it's a versatile, beginner-friendly language with a large, supportive community, making it a great choice for various applications, including web development, data science, and AI, and it opens doors to numerous career opportunities. 
### What is Python used for?
Python is a versatile programming language used for a wide range of applications, including web development, data science, machine learning, automation, and software development.
### Backslash characters and comments
Data type - integer, floating point/decimal,string

Backslash character/ Escape Sequences

              \n = new line
              
              \t = tab
              
              \" = "
              
              \' = '

### Basic Numerical Operations

              +

              -

              *

              /

              //(FLOOR)

              **(EXPONENTIATION)

### Relational Operator                               Boolean Values

             >                              True                               

             >=                             False

             <

             <=

             ==

             !=

## Control Statement 

Conditional control statement (if , elif , else)

Loop control statement(for , while)

## if statement syntex

 if expression:
 
     statements

## if , else syntax

  if expression:

    statements
    
  else:

    statements

**statement 1 -> if statement**

**statement 2 -> if statement ,else statement**

**statement 3 -> if statement , elif statement...... , else statement**

**inner if statement** also called **nested if statement**

## Logical Operator 

        and    or     not

## while loop

    i= 1
    
    while i <= 10
    
    print (i)
    
    i = i + 1
    
print ("End")

### Lamda Functions

A function without name(Anonymous Function).

Not Powerful as named Function.

It can work with single expression/ single line of code.

### Recursion

Recursion is a process where a function can call itself.

To stop calling we need a base case.

**important points in case of Recursion**

1. Recursive call
2. 
3. Base case

**Recursion example**

5! = 5*4*3*2*1

4! = 4*3*2*1

3! = 3*2*1

2! = 2*1

1! = 1

n! = n * (n-1)!


int fact(int n)

{
    //base case
    
    if(n==1)
    
          return 1;
          
    else
    
          return n * fact(n-1);

}


### Object Orianted Programming

1. Class

2. Object

3. Inheritance

      Hierarchical

      Multi-Level

      Multiple

 4. Abstraction

 5. Encapsulation

 6. Polymorphism


### Magic methods for comparison

__eq__(self,other)                for ==

__ne__(self,other)                for !=

__lt__(self,other)                for <

__gt__(self,other)                for >

__le__(self,other)                for <=

__ge__(self,other)                for >=


### Magic method for arithmetic calculation

__add__(self,other)

__sub__(self,other)

__mul__(self,other)

__div__(self,other)


### Regular Expression

Regular Expression are tools for manipulating string.

### We need Regular Expression because

     Verifying that strings match a pattern.

     performing substitutions in a string


Regular Expression can be accessed using the **re** module

     match() : matches at the beginning of a string.

     search(): finds a match of a pattern anywhere in the string.

     findall(): returns a list of all substrings that match a pattern.




             

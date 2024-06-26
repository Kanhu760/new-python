what is python ??

 -->python is simple, easy & Portable.

-->python is free & open sourse.

-->python is high level, interpreted language.

-->python was developed by Guido van Rosum.

-->python is interpreted language means when we write python code its executed the code line by line thats why we called python is interpreted language.

-->print is function to give output statement in python. simply we can tell "print" is output function.

Character set of python language :-

-->letter -> A-Z, a-z
-->Digits -> 0 - 9
-->Special character -> -,+,/,* etc..
-->Whitespaces -> Blank Space, Tab, newline.

what is variable in python :- a variable is a name given to a memory location in a program or else we can simply say varibale is a container to store some data.

-->example - name = "shradha" age = 23 salary = 23000.56

-->variable names - name, age, salary varibale values - "shradha", 23, 23000.56

Rules for Identifires :-

-->identifires - names of the variable
-->identifires can be combination of uppercase and lowercase letter, digits or an underscore(_). ex. - myVariable, variable_1
-->an identifires can not start with digit. so while variable1 is valid but 1variable in not valid.
-->we can not use special character or symbols like !,#,@,% etc...
-->identifires can be of any length.
-->variables name should be small and meaningful like - when we give our age in that case we take the variable as "myAge". myAge -> camel case letter.

'type' is a operator to show the datatypes name in our varibles like which datatypes we use in our variables.

Data Types :-
-->mainly data types of 5 types in python.
-->These data types are unmutable or build-in data types.
-->Integer - +ve value , 0 , -ve value.
-->String - "hello", "shradha" etc...
-->Float - 3.91, 4.00 , 9.1 etc..
-->Boolean - True , False.
-->None - not assign.

Comments in python :-

-->when we write some code but we dont want to execute it then we give the comment line to that place so that line of code will not executed.
-->comments are of 2 type.
-->single line comment - when we give the single line comments. in python we did it on "#". ex.

Single line comment:-
"this is a comment"

Multi line comment - when we gibve the multi line comment in python we did it through """-""". ex. """ multi line comments """

Types of Operator :-

Simply we can say operator is a symbol that performs a certain operation between operands. ex. a + b a,b 
-> operands
-> operator
-->there are 4 types of operator are present in python
-->Arithmetic operator. - (+,-,/,%,*)
-->Relational operator. - (==, != ,> ,<, >=,<=)
-->Assignment operator - (=, +=, -=, *=, /=, %=)
-->Logical operator - (and, or, not)

Input in Python :-

-->Input() statement is used to accept values(use keyword) from users.

Task to do for practice -
write a program to input 2 numbers & print their sum
Write a program to input side of a square & print its area.
write a program to input 2 floating point numbers & print their average.
write a program to input 2 int numbers a & b, print True if a is greater then or equal to . if not print false.

Strings :-
-->String is datatype that stores a sequence of characters.
-->str1 = "this is a good day" str2 = 'This is beautiful day' str3 = """this is a bad day"""

-->all these strings are real string because in python, it supports all of these syntax like - "", '',""" """

-->\n (new line) - when we want to break our line into a new line then we can give the new line symbol in that place so the line get breaked automatically.

Basic Operation of strings :-

concatenation -> "hello" + "world" ="helloworld"
Length of String -> len(str)

Indexing of string ->

-->webbocket -> 012345678(indexing)
-->Always indexing start from '0'.

Slicing of string ->

-->Accessing parts of a string.
-->ending index is not counting.
-->syntax - str[starting_index : ending_index]
-->str = "webbocket" str[0:3] - web str[:3] - web str[3:] - bocket.

Functions of string ->

-->ex- str = "i am a coder."

-->str.endswith("er.") - returns true if string ends with substring.
-->str.capitalize() - returns 1st char is capital.
-->str.replace(old,new) - replace all occurances of old with new.
-->str.find(word) - returns 1st index of 1st occurrence.
-->str.count("am") - counts the occurrence of substring in string.

Homework :-

write a program to input users first name & print its length.
write a program to find the occerrence of '$' in a string.

conditional statement :-

-->used to handle the condition in your program.
-->syntax (if-elif-else)
-->elif means else-if
-->if(condition): statement1 elif(condition): statement2 else: statement(default)

Homework :-

write a program to check if a number entered by the user if odd or even.
write a program to find the greatest of 3 numbers entered by the userd.
write a program to check if a number is a multiple of 7 or not.

Lists in Python :-

-->List is a built-in data type that stores set of values.
-->it can store elements of different types like integer, float & string etc..
-->in list we can make indexing.
-->in list we can find length of the list also.
-->in list we can also do the slicing activity.
-->ex- marks = [87, 45, 67, 83, 45] - array and list student = ["hitesh", 85, "bhubaneswar"] - list

List Slicing :-

-->it similar to string slicing.
-->syntax :- list_name[starting_idx : ending_idx]
-->ending index is not included.
-->marks = [23,25,67,78,98] marks[1:4] -> [25,67,78] marks[:3] -> [23,25,67] marks[2:] -> [67,78,98]

List Methods :-

-->list = [9,4,7,8,1] list.append(6) - adds one element at the end of the list - [9,4,7,8,1,6].
-->list.sort() - sort the elements in assending order - [1,4,7,8,9]
-->list.sort(reverse=True) - sorts the element in decending order - [9,8,7,4,1]
-->list.reverse() - reversing the list - [1,8,7,4,9]
-->list.insert(idx,el) - insert the element at index.
-->list.remove(1) - remove the firt occurrance of element - [9,7,8,1]
-->list.pop(idx) - remove element at index.

git :-

-->git is a open source repository system where we can save, manipulate, colaborate our code with any one else.
-->in our software era, everyone can use git system for their software development.
-->we also called git is a version control system.
-->git provides some tools to use their functionality and features ex - github, gitlab etc..

Dt---->14/06/2024

Tuple in Python :-

-->Tuple is a build in data type that lets us create immutable(the value can't be changeble) sequence of values.
-->ex. tup = (87,67,98,34,45)
-->tup[0] -> 87
-->tup[1] -> 67

we can do the tuple as.

1. tup1 = () -> empty tuple
2. tup2 =(1) -> integer
3. tup2 = (1,) -> a tuple
4. tup3 = (34,67,89,20) -> tuple
-->tuple ha also satisfy the slicing property.

Tuple methods:-->

-->tup.index(element)-->returns index of first occurrence.
-->tup.count(element)-->returns the count total occurence.


ex.  tup = (2,1,3,1)
     tup.index(1)-->1
     tup.conut(1)-->2
     tup.count(3)-->1


Dictionary in python:-->

-->Dictionary is ude to store the data Values in key:value pair.
-->They are unordered ,mutable(changeble) and dont allow duplicate keys.
ex-->
dict ={
    "name" : "shradha",
    "cgpa" : 9.8,
    "marks" : [98,97,96]
}
--> The left part of the dictionary are the keys and right side part in their values so dictionary contains key:value pair structure.

Nested Dictionary in Python:-->

-->Dictionary also satisfy the nested property.
-->Dictionary under dictionary is called nested dictionary.
-->ex....
student ={
    "name" : "Kanhu",
    "score" : {
        "chem" : 98,
        "math" : 97,
        "phy" : 87,
    }
}



Dictionary Methods:-->

1. myDict.keys()--it returns all keys.
2. myDict.values()--it returns all values.
3. myDict.items()--it will return all key:value pair as tuple.
4. myDict.get("key")--return the key according to values.
5.myDict.update(newDict)--insert the specified items to the dictionary.


Set in python:-->
-->set is the collection of the unordered items.
-->Each element in the set must be unique and imutable (can't change).
-->ex...

nums={1,2,3,4,5}
set2={5,8,9,4}

Set method:-->

1. set.add(element) --> adds an element.
2. set.remove(element) --> remove an element.
3. set.clear() --> clear all element.
4. set.pop() --> remove a random value of set.
5. set.union(set2) --> combine both set values and returns a new set.
6. set.intersection(set2) --> combine the common value and return a new set.

--> ex........

set1={1,2,3,2,4}
set2={3,7,2,6,4}
set1.union(set2)-->{1,2,3,4,6,7}
set.intersection(set2)-->{2,3,4}

Dt:-->17/06/2024

Loops in python:-->
-->Loops are used to repeat instruction.
-->In python there are 2 loops--while loop and for loop.

1. While loop-->
   Syntax-->
   Initialization
   while condition:
      statements
      increament/decrement.

Break and continue:-->

-->Break:Break is used to terminate the loop when encountered.
-->Continue:Terminates execution in the current iteration and continue execution of the lop with the next iteration.

2. For loop-->
-->For loop are used for sequential traversal,for traversing list,string,tuple etc..
-->Syntax:--
  for val in list:
  statement..



Home work:---->
1. Print the element of the following list using a loop.
[1,4,9,16,25,36,49,64,81,100]
2.Search for a number x in ths tuple using loop.
[1,4,9,16,25,36,49,64,81,100]


Dt:------>21/06/2024


Object oriented programming in python:-->

--To map with real world scenarios,we started using objects in code.  
--This is called object oriented programming(OOP).

1st concept:--> Procedural programming.
2nd concept:--> Functional programming.
3rd concept:--> Object oriented programming.

Class and Object in python:-->

--Class is a blueprint for creating objects.
ex:-->Creating a class .
class Student:
   name = "web bocket"

ex:-->creating a object(instance)
s1 = student()
print(s1.name)  #web bocket

___init___ Function(constructor):-->

--All class have a function called _init_(), which is always when the class is being initialised.

ex:--> creatinig a class 
class Student:
   def_init_(self,fullname)
     self.name=fullname

ex:-->creating a object
s1=Student("web bocket")
print(s1.name)

Note:-->The self parmeter is a referene to the current instance of the class and is used to access variable that belongs to the class.


Class and instance Attributes:-->

university --> college1,college2,college3,college4
               student1,student2,student3,student4

--colleges and students are the attributes of university.


Methods in python:-->
--Methods are function that belongs to objects.

ex:-->creating class
class Student:
  def_init_(self,fullname)
     self.name = fullname
  def hello(self):
     print("hello",self.name)

ex:-->creating object
s1 = Student("rohan")
s1.hello()

Dt:--->22/06/2024

Abstaction:--->

-->Hiding the implementdetails of a class and only showing the essential features to the user.


Encapsulation:-->

--Wrapping data and function into a single unit(object).

pratice question:-->

--Creat Account class with 2 attributes - balance and account no. and creat methods for debit,crredit and printing the total balance.


Dt-->24/06/2024

Private(like) Attribute and methods:-->

-->Private attributes and methods are meant to be used only withib the class and are not accessible from outside the class.
-->The private class attributes are written in__(attributes) so that we call it private attributes of a class.

Inheritance--->

-->When one class(child class) derives the properties and methods of another class(Parent class).
-->Syntax :--
class Car:
    --------
class ToyotaCar(car):
    --------

-->In python inheritance are 3 types:-
1. Single Inheritance.
2. Multi-level Inheritance.
3. Multiple Inheritance.

Dt:---->26/06/2024

Polymorphism :--->

Operator over loading:-->

--When the same operator is allowed to have different meaning accordingly to the context.
--In that polymorphism we can use Dunder function.
1. a + b ->__add__
2. a - b ->__sub__
3. a * b ->__mul__
4. a / b ->__truediv__
5. a % b ->__mod__

Ex:-->(+)
print(1 + 2) # 3(addition)
print("web" + "bocket") # web bocket(concatination)
print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6](merged)


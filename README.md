# CPSC 2030 (Lab_06)

Wednesday, February 28th

**Due**: By the end of the lab (Friday, March 8th)

**Instructions**  
For this lab, you will gain additional exposure to working with inheritance and polymorpishm in Python. To do this, we will simulate the beginning of a Learning Management System (LMS) that allows for you to create new classes and populate those classes with class resources (such as quizzes or assignments). I have provided you with `Canvas.py`, which relies on importing `Resource.py` and `Class.py`. I also have provided you with a colorized UML diagram, showing which classes belong in `Resource.py` (yellow) and which class belongs in `Class.py` (blue).

You should satisfy the following requirements:
- Implement the `ClassResource` class in `Resource.py` according to the UML diagram
  -  Create the __init__ method and overload the __str__ and __gt__ methods.
- Implement the `Quiz` class in `Resource.py` according to the UML diagram
  -  Inherit from `ClassResource`
  -  Extend the __init__ method and overload the __str__ and __gt__ methods.
    - __gt__ should compare the length of the questions lists 
  -  Add a new method `take_quiz` that prints the questions one at a time, captures and saves the user input in a list, then prompts for submitting the quiz (ultimately calling the private submit() method)
  -  Add a new method `submit` that takes a list of user answers and compares them to the private __answers property, returning a score out of 100.
- Implement the `Assignment` class in `Resource.py` according to the UML diagram
  -  Extend the __init__ method and overload the __str__ and __gt__ methods.
    - __gt__ should compare the due dates of the two assignments
 
- Implement the `Class` class in `Class.py` according to the UML diagram
  - Create the __init__method, with all the listed properties provided by the program, except for _resources which is an empty list.
  - Add a new method `add_resource` that takes an instance of `ClassResource` (whether quiz or assignment)
    - Prompt the user if they want to save: if yes, append to the _resources property
  - Add a new method `display_info` that prints a formatted string with all properties (except resources)
    - If the length of _resources is not zero, then call the protected `_display_resources()` function.  
  - Add a new method `_display_resources()` that iterates through the _resources property and prints the author, title, and created date.

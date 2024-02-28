from Class import Class
from Resource import Quiz, Assignment

if __name__ == "__main__":
    my_class = Class("Fundamentals of Computational Thinking and Problem Solving", "John Doe", "01/01/2024", "05/31/2024", 10)
    my_class.display_info()

    new_quiz = Quiz("Python 101 Quiz", "John Doe", "01/15/2021", ["What is Python?", "What data type uses square brackets?", "Is Python dynamically typed or statically typed?"], ["A programming language", "A list", "dynamically typed"])
    my_class.add_resource(new_quiz)

    grade = new_quiz.take_quiz()
    print(f"You received a {grade} on the quiz.")

    new_assignment = Assignment("Lab 06", "Jon Craton", "02/26/2024", "03/08/2024", "Polymorpism in Python", 1024)
    my_class.add_resource(new_assignment)

    another_assignment = Assignment("Lab 07", "Jon Craton", "03/04/2024", "03/08/2024", "ABCs in Python", 1024)
    my_class.add_resource(another_assignment)

    my_class.display_info()
    
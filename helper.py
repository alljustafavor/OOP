# When to use class methods and when to use static methods ?

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''
        pass
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do somethinf that has a relationship
        with the class, vut usually, those are used to 
        manipulate different structures of data to instantiate 
        objects, like we have done with the CSV.
        '''
        pass
# Breakdown of when to use class methods vs. static methods

'''
Class methods

    Use Cases:
        * Working with class attributes: When you need a method
        to access or change attributes that are shared by all instances of a class.

        * Factory methods: To create alternatice constructors for your class,
        allowing more controlled ways to create an instance.

    Signature: Class methods hace cls to the class itself as their first arguement
'''

# Example
class Employee:
    num_of_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_of_employees += 1

    @classmethod
    def get_employee_count(cls):
        return cls.num_of_employees

'''
Static Methods 
    
    Use Cases:
        * Utillity function related to the class: Methods thare are
        conceptually related to the class vut don't need to modify 
        class attributes or individual objects instances.

        * Namespacing: To group related function under the class name
        for organization, even if they don't directly interact with 
        class or object state.

        * Signature: Static methods don't have any special first argument(like self or cls)
'''

# Example

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

# Key Points To Help Choose
'''
    * Class Context: If the method needs to work with class-level
    attributes or create instances, use a class method

    * Object Context: Use instance methods when your method needs
    to operate on the specific state of an object.

    * Logical Grouping: If the method is related to the class but
    doesn't need to class or instance state, use static method.
'''

# Oop-s-Concepts

Class: A class is a collection of objects. It just does a classification, separation, and segmentation.

Objects: object is a real-world entity, real-time entity, actual data, or real function.

Constructor: This is a special method that is automatically called when an object of a class is created. Use to initialize the object's attributes and perform any necessary setup. It is responsible to provide data.
- constructor method:  __init__():  it is defined within a class and takes the "self" parameter as the first parameter.
- self: is a pointer. pointing to a particular class, this is the meaning of the first variable.
  class person:
      def __init__(self,---,---,---):

- Public: self.PublicVariableName = public
- private: self.__PrivateVariableName = private --(to call a private variable we have to use objname._classname__PrivateVariableName)
- protected: self._ProtectedVariableName = protected  --(to call a protected variable we have to use objname._protectedVariableName)

Inheritance: This is the capability of one class to derive or inherit the properties from another class. The class that derives the properties is called derived class or child class and the class from which the properties are being derived is called the base class or parent class. (class inside a class which inherits the properties of parent class)

Data Abstraction: Where we are trying to hide data behind someone/class. It restricts the user to access data directly.

Encapsulation: (Modification). The process of bundling data and methods together within an object, while hiding the internal implementation details and providing a defined interface for interaction

Polymorphism: function having different forms of performing different tasks in different situations or instances.

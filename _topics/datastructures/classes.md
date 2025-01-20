---
title: Python Classes
layout: default
jax: True
---
# Python Classes

Structures in C are similar to classes in Python (Classes in Python are actually much much more powerful, but that's not the point in this section). We can define a `Student` class in Python as follows,

```python
class Student:
  def __init__(self, name, gpa):
      self.name = name
      self.gpa = gpa
  
  def __str__(self):
      return self.name + ": " + str(self.gpa)
if __name__ == "__main__":
  s = Student('Fred', 3.7)
  print(s.name, s.gpa)
```

Here, `__str__` is a built-in function, and we can call it via either:

```python
s.__str__()
Student.__str__(s)
```

Here, the first line is just shorthand notation for the second line. What makes this built-in function useful is that we can call `print(s)` and it will treat this as `print(s.__str__())` instead.  
  
We can also write a function to compare two classes, so that we can use operators such as `<`, `>`, and `==`. For example,

```python
class Student:
  def __init__(self, name, gpa):
      self.name = name
      self.gpa = gpa
  
  def __str__(self):
      return self.name + ": " + str(self.gpa)
  
  def __lt__(self, other):
      # Return True if self has lower gpa than other
      # If GPAs are tied, compare names

      if self.gpa < other.gpa:
        return True
      elif self.gpa == other.gpa:
        return self.name < other.name
      else:
        return False
if __name__ == "__main__":
  fred = Student('Fred', 3.7)
  bob = Student('Bob', 2.0)
  print(Student.__lt__(fred, bob))
  print(fred < bob)
```

Recall that this is very similar to the compare function we wrote for `qsort.` Because we can compare different students, we can also sort them using the default sorted function in Python. For example,

```python
L = [Student("Fred", 3.7"), Student("Bob", 3.7), Student("Alice", 3.9)]
L.sort()
print(L) # [Bob: 3.7, Fred: 3.7, Alice: 3.9]
```

will allow us to sort and print out the list of students in a very convenient way (using both the custom print and compare functions we wrote)! Note that this is a more flexible method of sorting classes in Python. The "traditional" way (for simple comparison functions), we will write a function to get a numerical value from the class and sort using that key. For example,

```python
def get_name(s):
  return s.name
L.sort(key=get_name)
```

will sort the list of students in `L` alphabetically. Alternatively, we can use anonymous functions (lambda functions) which we can write in one line to save space. For example,

```python
L.sort(key=lambda s: s.name)
```

achieves the same purpose.  
  
However, it is difficult (but not impossible) to modify the "traditional" way and come up with a way to map a more complicated comparison function to a numerical value. Note: comparison functions can be as complex as we want, but they need to be _transitive_ in order to get meaningful results.

---
title: Structs and Type Definitions
layout: default
---
We have seen so far that C is a statically typed language with a set of variable types that it natively supports. What if we wanted to create our own? Or even group primitive types that related to each other? A student for instance, could be a variable that contains information such as their name, their major and the highest number of Valgrind errors achieved in one submission.

# Typedef

Firstly, let's look at how C treats data types. Suppose we are working with arrays on a project and we want to define the size of an array depending on the hardware we are running on; we can try
```c
typedef int arr_sz_t;
arr_sz_t sz_of_my_arr = 15;
```
Notice the suffix `_t`, this is an informal convention used to denote a data type related to the size of something in C. Now for any given reason, we can choose to define the size data type based on another primitive, eg
```c
typedef unsinged int arr_sz_t;
```
and the rest of our code should remain unchanged. 

# Structs
Now let's look at organising data types into a compound data type, like our student from above. Compound data types are implemented using structs (in other languages/paradigms you may hear the term 'object', though the two are not exactly the same). In C, it's useful to think about how a struct allocates all the necessary memory (plus some overhead) to store a compound data type. For example, our student might look like
```c
struct EngSci{
	char name[50];
	char student_ID[11]; // why do we need the 11th char?

	double GPA;
	unsigned long int valgrind_record;
}; // don't forget the last semicolon :))
```

Initialising a struct can be done in a few, creative, ways.
```
 struct EngSci s1 = {“John Doe”, “1234567890”, 3.3};  
 printf(“%s %f\n”, s1.name, s1.GPA);
```
Now technically, the data type we created is a `struct EngSci`, so a shorthand can instead be used when defining the struct
```c
typedef struct EngSci{
	char name[50];
	char student_ID[11];

	double GPA;
	unsigned long int valgrind_record;
} EngSci; 

// Now I can define in my main function
int main()
{
	EngSci s1 = {"John Doe", "1234567890", 3.3}; 
}
```
We can of course use pointers to keep track of dynamically allocated structs.

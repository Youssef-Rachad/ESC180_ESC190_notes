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

# Keeping track of strings in structs
## How does UofT make more students?
```c
struct student1{
  char name[200];
- double gpa;
};

struct student2{
  char *name;
- double gpa;
}
```
In the first implementation, we store exactly enough space for a name of 200 characters. This imposes a limitation on the maximum name length, and conversely also wastes space for names that do not occupy the full character allocation. In the second implementation, we store an address to a character, and pointers are fixed size. This allows us to be more effective with our memory usage provided we properly manage the memory allocated for the name field.

```c
void create_student1(struct student1 *p_p_s1, const char *Sname, double Sgpa)
{
  // Given the address to a student instance, allocate the required memory
  *p_p_s1 = (struct student1*)malloc(sizeof(struct student1));
  strcpy((*p_p_s1)->name, Sname);  // Grab the student then its name field (order of operations: -> has higher precedence than *)
                                   // Re: we rely on name being a 200 char array in this implementation
  (*p_p_s1)->gpa = Sgpa;
}

int main()
{
  struct student1 *p_s1;  // This is the address of a student , 
                          // which is not instantiated in memory yet
  create_dtudent1(&p_s1, "Mike", 9000);
}
```

A note on when to use the arrow operator and when to use the dot operator to access a field:
- If using the struct itself then the dot is used 
- If using the pointer to a struct, the pointer does not need to be dereferenced. Instead the arrow operator takes care of dereferencing the pointer and accessing the field appropriately.
so `p_struct -> field` is the same as `(*p_struct).field` and `struct.field`

```c
void create_student2(struct student2 *p_p_s2, const char *Sname, double Sgpa)
{
  // Given the address to a student instance, allocate the required memory
  *p_p_s2 = (struct student2*)malloc(sizeof(struct student2));
  (*p_p_s2)->name = (char *)malloc(sizeof(char) * (strlen(Sname) +1)); // +1 for \0 
  
                                   // Re: we need to allocate a char array in this implementation
  strcpy((*p_p_s1)->name, Sname);
  (*p_p_s1)->gpa = Sgpa;           // No need to allocate memory since we already have enough space to store a double
}

int main()
{
  struct student1 *p_s1;  // This is the address of a student , 
                          // which is not instantiated in memory yet
  create_dtudent1(&p_s1, "Mike", 9000);
}
```
In the second implementation, directly using `strcpy` without allocating enough space for the name leads to undefined behaviour.

# Managing an array of student structs
## ALL the students
```c
void create_student2_array(struct student2 **p_p_s2, int n_students)
{
  // Given the address to a student array, allocate the required memory
  *p_p_s2 = (struct student2*)malloc(sizeof(struct student2) * n_students); // Allocating an array of students means allocating enough memory for n students
  (*p_p_s2)->name = (char *)malloc(sizeof(char) * (strlen(Sname) +1)); // +1 for \0 
  // The result is that 
  //   (*p_p_s2)[0] is the address to the first student
  //   (*p_p_s2)[1] is the address to the second student
  // and so forth (syntactic suger for pointer arithmetic)

  // At this point, we have enough allocated space for a pointer to a name and a gpa
  // but dereferencing the name pointer is not defined behaviour since no memory is allocated
  // One possibility is to allocate some fixed memory and to potentially change it if needed afterwards
  for(int idx = 0; idx < n_students; i++){
    (*p_p_s1)[i].name = (char *)malloc(sizeof(char) * 100);
  }
}

int main()
{ 
  struct student1 *p_s1;  // This is the address of a student , 
                          // which is not instantiated in memory yet
  create_dtudent1(&p_s1, "Mike", 9000);
}
```

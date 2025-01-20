---
title: Strings
layout: default
jax: True
---
# Strings
Strings in C can be a bit tricky at first because a lot of abstraction is not immediately built into the language. We will see how a string is derived from the primitive type `char` and we will implement some string functions while exploring the `<string.h>` where a standard implementation of most string operations is provided by the language.
# The `const char*` type
When we pass a string directly into a function, for example in `printf("I love ESC190");`, we don't think about the datatype of the string and often confuse it. In fact it is a `const char*` which means: 'a pointer to an array of characters which are constant'. 
This is more relevant in the following example
```c
int main()
{
  const char* course = "ESC190";
  return 0;
}
```
Here, `course` is a string in the sense that it is a pointer to an array of characters. The pointer points to location in memory but the contents of that contiguous block of memory cannot be changed, hence it is immutable.
The compiler gives an error whenever the contents are modified in any way.
```c
int main()
{
  const char* course = "ESC190";
  course = "ESC102";              // Error
  return 0;
}
```
Let's see other ways of declaring strings such that we can manipulate them more flexibly.
# Static Strings
By definition, a string is an array of characters so naturally we could declare a string as follows:
```c
int main()
{
  char course[] = {'P', 'R', 'A', 'X', 'I', 'S', '\0' };
  printf("My next lecture is %s", course); // we %s to format a string
}
```
Notice the trailing `\0` character called the terminator. We say that strings are null-terminated and this lets the compiler know how much memory the string occupies. 
In essence, accessing a string variable involves the compiler locating a character in memory and reading the adjacent character in order until the null-terminator tells it to stop reading.

Of course, we can use a shorthand called a string literal which comes with a built-in null-terminator
```c
int main()
{
  char course[] = "PRAXIS";
  printf("My last lecture was %s", course);
}
```
Notice that characters are enclosed in single quotes ( ' ) while strings are enclosed in double quotes ( " ). This syntax is enforced by the compiler. Since strings are arrays, we can access them similarly
```c
int main()
{
  char course[] = "PRAXIS"
  for(int idx = 0; i <= 7; i++) {
    printf("%c", course[idx]);   // The output will be:
                                 // P
                                 // R
                                 // A
                                 // X
                                 // I
                                 // S
                                 // \0
  }
}
```
# Dynamic Strings
We found that static strings are mutable, which is a nice feature for changing the actual content but still does not allow us to modify the length of the string. In fact, statically allocated memory cannot be resised in C. To overcome this, we dynamically allocate memory large enough to hold some characters and assign the first letter to a pointer:
```c
int main()
{
  char *mystr = (char *)malloc(20 * sizeof(char));
}
```

This allows us to construct a string with similar functionality to strings as defined in Python [DynamicString]({{ site.baseurl }}{% link _topics/datastructures/dynamicstring.md %})

# String Operations
coming soon..


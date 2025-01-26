---
title: Exercise 1
layout: default
jax: True
---
# Exercise 1

{% include quiz.html 
   question="
   Write a function which changes the value of `a`:
   ```c
#include <stdio.h>
void change_a(...)
{
  ...
}

int main()
{
  int a;
  change_a(...);
  printf(\"The value of a is %d\", a);
  return 0;
}
   ```
   " 
   answer="
   We need to pass the address of `a` using the addressof operator: `&`.
   ```c
#include <stdio.h>
void change_a(int *p_a, int value)
{
  *p_a = value;
}

int main()
{
  int a;
  change_a(&a, 42);
  printf(\"The value of a is %d\", a);
  return 0;
}
   ```
   " 
%}

{% include quiz.html 
   question="
   Write a function which does NOT change the value of `a`:
   ```c
#include <stdio.h>
void dont_change_a(...)
{
  ...
}

int main()
{
  int a;
  dont_change_a(...);
  printf(\"The value of a is %d\", a);
  return 0;
}
   ```
   " 
   answer="
   We can pass the value of `a` as usual since it will be copied into the function scope.
   ```c
#include <stdio.h>
void dont_change_a(int a, int value)
{
  a = value;
  printf(\"In the functio scope, the value of a is %d\", a);
}

int main()
{
  int a = 24;    // We need to initialise the value of a before printing it 
  dont_change_a(a, 42);
  printf(\"The value of a is %d\", a);
  return 0;
}
   ```
   " 
%}


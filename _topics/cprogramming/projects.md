---
title: Projects
layout: default
---
# The Command Line
So far we discussed how to write a simple C program but how do we actually run it on our machines. In essence, we give a C compiler the list of all the files we need and instruct it to build a binary executable. This can all be done on the command line, and while there are more advanced ways of building a project, let's see how to do this for a simple program and increase the complexity from there.

_We are now working in the command line, go ahead and open your favourite terminal and follow along!_

The assumption is that you are working with a UNIX machine (macOS or Linux) or using Powershell on Windows. There are many terminals for you to explore but the rule of thumb is to not use Windows Command Prompt because it is incompatible and a hassle to teach.
# Filesystem Basics
First, we need to understand how to use the file system. This means locating the directory where our code files live and potentially making new directories. There is much more to do in the filesystem but the following is meant to get you started and provide the necessary information for ESC190.

Suppose I have the following structure
```
Courses
  |- ESC180
      |- Project1/
      |- Project2/
      |- hello_world.py
  |- ESC190
      |- Project1/ 
      |- Project2/
      |- astar.py
```
and I am currently in the ESC190 directory
### Where are we?
Type `pwd` to print your current working directory. `pwd` literally stands for print-working-directory.
```shell
# check the current directory
pwd
# C:\Users\Youssef\Courses\ESC190 
```
### What files are in this directory?
Type `ls` to list all the files in the current directory. If you specify a path argument, you can list the files in the chosen path. 
```shell
# list files in the current directory (C:\Users\Youssef\Courses\ESC190)
ls 
ls .

# list files in a sub-directory       (C:\Users\Youssef\Courses\ESC190\Project1)
ls Project1

# list files in the parent folder     (C:\Users\Youssef\Courses\ESC190)
ls ..
# one more level above                (C:\Users\Youssef)
ls ../..

# list files in an adjacent directory (C:\Users\Youssef\Courses\ESC180)
ls ../ESC180
```
_Fun Fact_ `ls` is short for list.
### Moving around
Using `cd` and similar arguments from above, we can change the current directory instead of simply listing it. `cd` stands for change-directory.
### Endless directories
And finally, `mkdir` creates a new directory. The command name is short for make-directory.
# Compiling a program
Now type `gcc -Wall -std=c99 -o myprogram filename.c`. Here: 

- `-Wall` tells the compiler to show all warnings
- `-std=c99` tells the compiler to use the C99 standard and
- `-o myprogram` tells the compiler to output the program as `myprogram`. 

You can name the program whatever you want, but it's good to name it something that is descriptive of what it does. On Windows, you will need to name it `myprogram.exe` instead.
# Execution
On Linux or Mac, you can run the program by typing `./myprogram`. On Windows, you can run the program by typing `./myprogram.exe`.

# Headers
Next, how do we use header files? Header files are a way to organize code. We can put all of our function and struct declarations in a header file, and then include it in our main program. This way, we can keep our code organized and we don't have to worry about forgetting to include a function or struct declaration in our main program. To do this, we can create a file called `my_struct.h` and put all of our declarations in there. Then, we can include it in our main program by typing `#include "my_strct.h"`.

For example, suppose that we are developing some kind of device that logs data. During prototyping we might want that log to be printed to our screen but when we deploy our device we have to write the output to a file that we can retrieve later on. 

Here's how we might define the header file
```c
// logger.h
#ifndef LOGGER_H // This makes sure we only load the header once
#define LOGGER_H 

void log_message(const char *message); 

#endif // LOGGER_H
```
Now we can implement the logging for debug
```c
// terminal_logger.c 
#include "logger.h" 
#include <stdio.h> 

void log_message(const char *message) 
{ 
	printf("Console Log: %s\n", message); 
}
```
And another version for the device when deployed
```c
// file_logger.c 
#include "logger.h" 
#include <stdio.h> 

void log_message(const char *message) 
{ 
	FILE *file = fopen("log.txt", "a"); 
	if (file != NULL) { 
		fprintf(file, "File Log: %s\n", message); 
		fclose(file); 
	} 
}
```
Now our main program doesn't need to account for which logger we are using
```c
// main.c 
#include "logger.h" 

int main() 
{ 
	log_message("EngSci is not English Sciences."); 
	return 0; 
}
```
However, we can build this project for either use case:
1. If debugging, the compilation is done via `gcc -o main main.c terminal_logger.c`
2. If deploying we instead compile `gcc -o main main.c file_logger.c`
and we are good to go!

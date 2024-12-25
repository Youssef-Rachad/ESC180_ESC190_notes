---
title: The C Programming Language
layout: default
---
> We learn C to learn how computers work. "Premature optimisation is the root of all evil." 
> 
> - Donald Knuth


# The C Programming Language
Generally speaking, we categorise computer languages as either high or low level depending on how much abstraction is built into the language. 
![[Pasted image 20240628203956.png]]
Python is an interpreted language which means that a python script is read block by block or line by line by the Python interpreter and command are executed as they are read. Note that the Python interpreter itself is a program. 

This is in contrast to C which is a compiled language. The compiler (often gcc, clang, llvm or msvc) compiles C source code into an executable that can almost directly be executed by your computer; i.e. without an interpreter. We call this computer hardware level instructions `machine code`, these contain very simple instructions such as moving values in memory, adding numbers and jumping to instructions based on conditions. Note that while the source code you write is human-readable (in theory - in practice readability depends on you), machine code is designed for the computer and is very impractical to read though it is executed much faster than interpreted code.

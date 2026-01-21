---
title: ESC190-Homepage
layout: default
---

# ESC190 Lecture Notes
These are official course notes for ESC190: Computer Algorithms and Data Structures.
<!--<br><br>-->



I will do my best to update notes within 24 hours of the lecture recording being posted. If you have any
feedback, questions, clarifications, or if you see a typo or a mistake, feel free to email me at <a
href="mailto:youssef.rachad@mail.utoronto.ca">youssef.rachad@mail.utoronto.ca</a>. Thanks to QiLin for
starting the notes!
<!--<br><br>-->



Cheers!

Youssef


# Table of Contents
- [Introduction to Programming in C](./topics/cprogramming.html)
- [Data Structure](./topics/datastructures.html)
- [Algorithms](./topics/algorithms.html)

# Lecture Calendar
<ol id="lecs">
  <li>Jan 5, 7 & 8 - Introduction to C <br><i>Note: the early concepts are reviewed often, the timestamps show when they are introduced while the notes are a synthesis of the material presented in lecture.</i>
	  <ul>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/thecprogramminglanguage.html">The C Programming Language</a> (
          <a href="https://www.youtube.com/live/C_s5KK_S2Zo?t=1011">Jan 5</a>
          )</li>
          <!-- https://www.youtube.com/live/0MszyVSEF_0?t=2768 -->
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/helloworld.html">Hello World</a> (
          <a href="https://www.youtube.com/live/C_s5KK_S2Zo?t=1011">Jan 5</a>,
          <a href="https://www.youtube.com/live/LZAW_4JvdIg?t=260">Jan 7</a>
          )</li>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/datatypes.html">Data Types</a> (
          <a href="https://www.youtube.com/live/C_s5KK_S2Zo?t=1434">Jan 5</a>
          )</li>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/strings.html">Strings</a> (
          <a href="https://www.youtube.com/live/C_s5KK_S2Zo?t=2037">Jan 5</a>
          )</li>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/arrays.html">Arrays</a> (
          <a href="https://www.youtube.com/live/C_s5KK_S2Zo?t=2700">Jan 5</a>,
          <a href="https://www.youtube.com/live/LZAW_4JvdIg?t=260">Jan 7</a>
          )</li>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/pointers.html">Pointers</a> (
          <a href="https://www.youtube.com/live/LZAW_4JvdIg?t=1569">Jan 7</a>
          )</li>
		  <li> &#x2514;&gt; <a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/pointers.html">Pointer Arithmetic</a> (
          <a href="https://www.youtube.com/live/Ya3t_hutkVc?t=1900">Jan 8</a>
          )</li>
		  <li><a href="https://docs.google.com/document/d/1ArkXvLQUWFbHNb_wwd_cdTB9RoOHKF0usXx7p1Bf-H4/edit?usp=sharing">Memory Model Sheet</a> (
          <a href="https://www.youtube.com/live/LZAW_4JvdIg?t=1647">Jan 7</a>,
          <a href="https://www.youtube.com/live/Ya3t_hutkVc?t=670">Jan 8</a>
          )</li>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/functions.html">Functions</a> (
          <a href="https://www.youtube.com/live/LZAW_4JvdIg?t=2120">Jan 7</a>
          )</li>
		  <li> &#x2514;&gt; <a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/functions.html">Passing Arguments by Value and by Reference to Functions</a> (
          <a href="https://www.youtube.com/live/Ya3t_hutkVc?t=1525">Jan 8</a>
          )</li>
		  <li> &#x2514;&gt; <a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/exercice.html">Exercises</a> (Jan 8)</li>
	  </ul>
  </li>
  <li>Jan 12, 14 & 15 - Pointers, Functions, Strings, Struct and Memory
     <ul>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/pointers.html">Pointer</a> (
          <a href="https://www.youtube.com/live/QgstsM8puKA?t=133">Jan 12</a>
          )</li>
          <li><a href="https://cpointerdrills.github.io/">Pointer Drills 1-10(ext.)</a>, <a href="https://dl.acm.org/doi/pdf/10.1145/3724389.3731268">link to paper</a> (
          <a href="https://www.youtube.com/live/CB1K-A91fpI?t=839">Jan 14</a>
          )</li>
          <li><a href="https://www.youtube.com/live/QgstsM8puKA?t=701">Example of Using GCC & VSCode</a> (Jan 12)</li>
          <li>Strings</li>
          <ul>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/strings.html">const char * and String Literals</a> (
          <a href="https://www.youtube.com/live/QgstsM8puKA?t=1228">Jan 12</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/strings.html">strlen</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=2197">Jan 15</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/strings.html">Modifying Strings</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=1971">Jan 15</a>
          )</li>
          </ul>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/helloworld.html">Using the Standard Output and printf()</a> (
          <a href="https://www.youtube.com/live/CB1K-A91fpI?t=2884">Jan 14</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/structs.html">Custom Data Types</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=713">Jan 15</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/structs.html">Structs and Compound Data Types</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=822">Jan 15</a>
          )</li>
		  <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/functions.html">Review: Passing Arguments by Value and by Reference to Functions</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=1458">Jan 15</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/arrays.html">Allocating Memory Blocks</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=2240">Jan 15</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/datatypes.html">sizeof</a> (
          <a href="https://www.youtube.com/live/0MszyVSEF_0?t=2870">Jan 15</a>
          )</li>
      </ul>

  <li>Jan  19, 21 & 22 - Arrays, Structs, Memory, Strings, Pointers, Working with Projects
	  <ul>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/structs.html">Calculating the Size of Compound Data Types</a> (
          <a href="https://www.youtube.com/live/FJ_5YqDLEhk?t=525">Jan 19</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/arrays.html">Counting the Elements of an Array</a> (
          <a href="https://www.youtube.com/live/FJ_5YqDLEhk?t=742">Jan 19</a>,
          <a href="">Jan 21</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/arrays.html">Allocating Memory Blocks</a> (
          <a href="https://www.youtube.com/live/FJ_5YqDLEhk?t=1138">Jan 19</a>,
          <a href="">Jan 21</a>
          )</li>
          <li><a href="https://cpointerdrills.github.io/">Pointer Drills continued (ext.)</a> (
          <a href="https://www.youtube.com/live/FJ_5YqDLEhk?t=2614">Jan 19</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/strings.html">String Methods</a> (
          <a href="">Jan 21</a>
          )</li>
          <li><a href="">Pointers to Pointers</a> (
          <a href="">Jan 22</a>
          )</li>
          <li><a href="{{ site.url}}{{ site.baseurl }}/topics/cprogramming/projects.html">Using GCC, Header Files, Pre-Processor</a> (
          <a href="">Jan 22</a>
          )</li>
	  </ul>
  </li>
  <!--<li>Jan 13 - <a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/exercice.html">Exercise 1</a>: Passing by reference and by value</li>
  <li>Jan 15 - Strings and pointers. Exercise 2: <a href="https://www.cs.toronto.edu/~guerzhoy/190/pointers" target="blank_">Pointers</a>  
       <ul>
           <li>Mutability of strings</li>
           <li>const char * type and read only memory</li>
       </ul> 
  </li>
  <li>Jan 16 -
      <ul>
          <li>const char * correctness</li>
          <li>printf formatting</li>
          <li>custom and compound data types with typedef and struct</li>
          <li>passing arrays to functions</li>
      </ul>
  </li>
  <li>Jan 20 - 
      <ul>
          <li>structs and memory usage</li>
          <li>pointers to structs</li>
      </ul>
  </li>
  <li>Jan 22 - </li>
  <li>Jan 23 - </li>
  <li>Jan 27 - String Methods:
      <ul>
          <li>strcpy</li>
          <li>??</li>
      </ul>
  <li>Jan 29 - Memory Management, String Methods
      <ul>
          <li>realloc</li>
          <li>error checking</li>
          <li>strcat</li>
      </ul>
  <li>Jan 30 - Increment/Decrement Operators, String Methods, Structs (and in arrays)
      <ul>
          <li> ++, -- and precedence</li>
          <li>Iterating through strings in increasingly silly ways</li>
          <li>strcpy</li>
          <li>length of string??</li>
          <li>storing strings in structs</li>
          <li>arrays of structs</li>
      </ul>
  <li>Feb 10 - <a href="{{ site.baseurl }}{% link _topics/datastructures/betterstring.md %}">Better Strings</a> in C
      <ul>
          <li> Creating, changing, appending and destroying</li>
      </ul>
  <li>Feb 12 - 
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/datastructures/betterstring.md %}">Better Strings</a> in C: `get_char`, `get_str`.</li>
          <li>What are <a href="{{ site.baseurl }}{% link _topics/datastructures/ADT.md %}">Abstract Data Types</a>?</li>
          <li>Example: <a href="{{ site.baseurl }}{% link _topics/datastructures/ADT.md %}">Lists</a></li>
          <li><a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/exercice.html">Exercise 1</a>: Is it an ADT or a DS?</li>
      </ul>
  <li>Feb 13 - 
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/datastructures/pyInteger.md %}">Pythonic Integers</a> in C.</li>
      </ul>
  <li>Mar 5 - Dynamic Programming Introduction
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}">Dynamic Programming Intro</a>.</li>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}#memoising-fibonacci-numbers">Fibonnaci Numbers</a>.</li>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}#painting-the-whole-neighbourhood">House Painting</a>.</li>
      </ul>
  <li>Mar 6 - Dynamic Programming House Painting
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}#painting-the-whole-neighbourhood">House Painting</a>.</li>
      </ul>
  <li>Mar 10 - Dynamic Programming Problems
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}#memoising-fibonacci-numbers">Fibonnaci Numbers</a>.</li>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}#painting-the-whole-neighbourhood">House Painting</a>.</li>
          <li><a href="">Coin Change</a>.</li>
          <li><a href="">Word Segmentation</a>.</li>
      </ul>
  <li>Mar 12 -
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/datastructures/graphs.md %}">Graphs</a>.</li>
          <li><a href="{{ site.baseurl }}{% link _topics/datastructures/stacks.md %}">Stacks</a>.</li>
      </ul>
  <li>Mar 13 -
      <ul>
      </ul>
  <li>Mar 17 -
      <ul>
          <li><a href="{{ site.baseurl }}{% link _topics/algorithms/dynamicprogramming.md %}#memoising-fibonacci-numbers">Fibonnaci Numbers Iteratively</a>.</li>
      </ul>-->
<!-- markdown auto closes the list maybe </ol> -->

---
title: Hashing
---
This lecture will cover the basics of how dictionaries work.
Hashing is the basic concept behind python dictionaries (also c++ maps but you don't need to know that!). Here we will see how hashing is different from simply storing elements in an array and the advantages we can draw in terms of element look up time complexity.


{{site.data.alerts.note}}
A **map** is a collection of _(key, value)_ pairs, where the keys are unique, but the values may not be. The two operations are:

- `get(key)` gets the value at the specific key
- `put(key, value)` puts the pair (key,value) in the map

_The term map also highlights the relationship between the keys and the values. You might have seen in MAT185 that mappings can be injective, surjective, bijective. In general, the map ADT is surjective (anything not in the values can be ignored) but not necessarily injective (hence why multiple keys can point to the same value)._
{{site.data.alerts.end}}

<u>For example, a python dictionary is an implementation of a map. How can we implement this?</u>

We can use a binary tree (specifically an AVL tree, don't need to know this). The pairs are stored as entries on this tree, sorted using a function that compares the keys. The operations $\verb #get#$ and $\verb#put#$ take $\mathcal 𝑂(\log⁡ 𝑛)$ time.

Use an array of values. We permit only integer keys and if the integers are big, the array may need to be large. If I want to store 100 pairs but one of my keys is 10000, then my array will have a size of at least 10000! The advantage is takes constant time for get and put.

Use hash tables. This is an extension of the array idea, but we don't need very large arrays, and keys are no longer limited to integers!

## Hash Tables

To implement a hash table, we can define a table (i.e. an array) of length $\verb#TableSize#$. Then we can define a function `ℎ𝑎𝑠ℎ(𝑘𝑒𝑦)` that maps keys to integer indices in the range $0,\dots,\verb#TableSize#-1$. Assuming that `ℎ𝑎𝑠ℎ(𝑘𝑒𝑦)` takes constant time, then we can implement the  $\verb #get#$ and $\verb#put#$ operations in constant time. Specifically, we ideally want this function to be an **injection.** In other words, there is a one-to-one map between keys and indices. This is because if we have two keys that map to the same index, then we have a collision.  
  
However, in reality this is not possible. There is a [countably](https://en.wikipedia.org/wiki/Countable_set) infinite number of keys, but only a finite  $\verb#TableSize#$ entries in the array. This isn't that bad though! For the most part, we can try to avoid collisions by distributing items evenly, and if there are collisions, we just need to find a way to resolve them.

## Hash Functions

From now on, we'll be working with integer keys. If we have a string as a key, we can simply convert it to its ASCII value. Remember from before that we want to save space, so we want to make  $\verb#TableSize#$ as small as possible, and for that reason, the hash function $ℎ𝑎𝑠ℎ(𝑥)=𝑥$ is bad. Instead, we can try $$ℎ𝑎𝑠ℎ(𝑥)=𝑥\ \%\ \verb#TableSize#$$where the symbol % is the modulo operator. This is a good hash function because it maps all integers to the range $0,\dots,\verb#TableSize#-1$. However, it's not a good hash function because it's not an injection. For example, if we have a table of size 10 and we have the keys $\{0,10,20,30,\dots,90\}$, then they will all map to the same index.  
  
Therefore, this hash function is only good if the keys we are working with are well distributed, in the sense that the hash function will map them to a relatively even distribution.  
  
If the key is a compound object (i.e. using a tuple as a key), we can construct the hash function$$ℎ𝑎𝑠ℎ(𝑠,𝑥)=(hash_1(s)\times p_1+hash_2(x)\times p_2)\ \%\ \verb#TableSize#$$where $𝑝_1$ and $𝑝_2$ are two prime numbers. The reason we want $𝑝_1$ and $𝑝_2$ to be prime is so that we don't have empty space. If they shared a factor, i.e. the number 2, then it would be possible that we're skipping all the odd cells in the table.

## Collisions (Chaining)

No matter how good our hash function is, we'll always have collisions. How can we deal with them? One method is via **separate chaining**. The idea is that we can keep all the items that map to the same index in a linked list.  
  
The runtime depends on the number of elements in a list on average. We can define the **load factor**$$\lambda=\frac{𝑁}{\verb#TableSize#}$$where $N$ is the total number of entries. It represents the average number of items in a linked list. While the worst-case run time is still $\mathcal O(𝑛)$, because everything could collide with everything. However, if we have a good hash function and everything is distributed evenly, then the average run time is $\mathcal O(\lambda)$. This is because if we're trying to lookup an item and it fails, we need to search all the nodes to ensure that, which is $\lambda$ operations. If it succeeds, then on average we need to perform $\lambda/2$ operations. Either way, we get $\mathcal O(\lambda)$. 
  
To ensure that we still have constant time operations, we want $\lambda\approx1$ and we increase the table size whenever needed. However, we can't simply _only_ double the size of the table, because the same hash function will no longer work for the keys stored previously. This is because the hash function depends on the table size! To resolve this, we'll double the table size and then rehash all the keys.

## Collisions (Probing)

Another way to deal with collisions is via **probing**. The idea is that we don't store the items in a linked list, but instead we store them in the table itself. If there is a collision, we can try to find another empty cell to store the item.  
  
For example, if we have **linear** probing, whenever we have a collision, we can try to store the item in the next cell. If that cell is occupied, then we try the next cell, and so on. This is easy to implement but in practice, it's not very good. The reason is that if we have a lot of collisions in close proximity to each other, it creates a cluster of occupied slots, making it more likely for subsequent collisions to occur in the same cluster, further exacerbating the problem.  
  
==There are more advanced methods of probing that can fix this issue.  ==
  
The loading factor $\lambda$ can be defined the same way, but note that with probing, we have $$\lambda\le1$$and the table is full if $\lambda=1$. Therefore, the interpretation is slightly different.
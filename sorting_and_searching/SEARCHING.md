## Searching:
- **Sequential search + implementation**
- **Binary search + implementation**
- **Hashing, hash tables + implementation**

In pythong we can use in operator to search for elements in a list:
```
>> 15 in [4,5,15,3]
True
```
How does the underlying process actually work?
And what's the best way to searh for things algorithmically?

### 1. Sequential search

Basic searching technique. Sequentially go through the data structure, 
comparing elements as you go along.
For instance, if you're searching for element 50, then you'll have to compare it with every element in the list.

Analysis for unordered list:
Case:             Best case:   Worst case:  Average case:
item is present       1             n           n/2
not present           n             n           n

Analysis for ordered list:
Case:             Best case:   Worst case:  Average case:
item is present       1             n           n/2
not present           1             n           n/2

### 2. Binary search

Starts by examining the middle item. If the item we are searching for is greater than the middle item, 
we know that the entire lower half of the list as well as the middle itm can be eliminated from further consideration.
Basically we either find it or split the list in half, therefore eliminating another large part of our possible search space.

Comparison    Apprx number of items left
1             n/2
2             n/4
i             n/2i

Analysis:
Case:             Best case:   Worst case:  Average case:
item is present       1           log n         log n
not present           1           log n         log n

Worst-case space complexity	O(1)

### 3. Hashing 

**_Hashing:_** Could be searched in O(1) time. This concept is referred to as hashing.

**_Hash tables:_** Each position of the hash table, slots, can hold an item and is named by an integer value starting at 0.
For example, we will have a slot named 0, a slot named 1, a slot named 2, and so on.
Initially, the hash table contains no items so every slot is empty. 

**_Hash functions:_**
The mapping between an item and the slot where that item belongs in the hash table is called the hash function. 
The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1. 
Most commonly used Remainder Method: 
*H(item) = item%11*
Load factor *λ = (number of items) / (table size)*
When we want to search for an item, we simply use the hash function to compute the slot name for the item 
and then check the hash table to see if it is present. 
This searching operation is O(1), since a constant amount of time is required to compute the hash value and then 
index the hash table at that location. 

**_Collision resolution_**
What if you have two items that would result in the same location? For example 44%11 and 77%11 are the same.
This is known as a collision (also known as a clash). 

A hash function that maps each item into a unique slot is referred to as a perfect hash function.
Our goal is to create a hash function that minimizes the number of collisions, is easy to compute, 
and evenly distributes the items in the hash table. 

Let’s discuss a few techniques for this:
- **The folding method** for constructing hash functions begins by dividing the item into equal-size pieces 
(the last piece may not be of equal size). These pieces are then added together to give the resulting hash value.

If our item was the phone number 436-555-4601
1. We would take the digits and divide them into groups of 2 (43,65,55,46,01). 
2. After the addition, 43+65+55+46+01, we get 210. 
3. If we assume our hash table has 11 slots, then we need to perform the extra step of dividing by 11 and keeping the remainder. 
4. 210 % 11 is 1, so the phone number 436-555-4601 hashes to slot 1.
- For the **mid-square method** we first square the item, and then extract some portion of the resulting digits. 

For example, if the item were 44 
1. we would first compute 442=1,936.
2. By extracting the middle two digits, 93, and performing the remainder step, we get 93%11 =5
- **Non-integer elements**
The word “cat” can be thought of as a sequence of ordinal values.
```
>>> ord("c")
99
>>> ord("a")
97
>>> ord("t")
116
```
1. 99+97+116 = 312
2. 312%11 = 4

**Collision resolution technique**

- **Open addressing**
It looks into the hash table and tries to find another open slot to hold the item that caused the collision. 
We could start at the original hash value position and then move in a sequential manner through the slots until 
we encounter the first slot that is empty. The general name for this process of looking for another slot after a collision is **rehashing**. 
  - **Linear probing**
  By systematically visiting each slot one at a time, we are performing an open addressing technique called linear probing.
  - **Quadratic probing**
  Instead of using a constant “skip” value, we use a rehash function that increments the hash value by 1, 3, 5, 7, 9, and so on. This means that if the first hash value is h, the successive values are h+1, h+4, h+9, h+16, and so on.
- **Chaining**
An alternative method for handling the collision problem is to allow each slot to hold a reference to a collection (or chain) of items.
As more and more items hash to the same location, the difficulty of searching for the item in the collection increases.


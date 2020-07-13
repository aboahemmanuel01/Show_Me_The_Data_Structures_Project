# Overview - Data Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). 
The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. 
The sender encodes the data, and the receiver decodes the encoded data. 

As part of this project, I was supposed to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, 
there is a loss (lossy) or no loss (lossless) of information. 
The Huffman Coding is a lossless data compression algorithm. 

## A. Huffman Encoding
There are two phases in encoding, which are:
`Building the Huffman tree (a binary tree)`, and `generating the encoded data`. 

## B. Huffman Decoding
After encoding the data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:
``
1 Declare a blank decoded string
2 Pick a bit from the encoded data, traversing from left to right.
3 Start traversing the Huffman tree from the root.
    If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
    If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
4 Repeat steps #2 and #3 until the encoded data is completely traversed.
```

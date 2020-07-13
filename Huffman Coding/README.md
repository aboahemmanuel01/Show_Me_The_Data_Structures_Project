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

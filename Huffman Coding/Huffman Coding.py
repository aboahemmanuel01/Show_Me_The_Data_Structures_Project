import sys
import heapq

class Huff_Node(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __gt__(self, other):
        if other is None:
            return -1
        if isinstance(other, Huff_Node) is None:
            return -1
        return self.freq > other.freq

class Huffman_Code(object):
    def list_of_frequency(self, text):
        freq_map = {}
        for char in text:
            if not char in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        return freq_map

    def sort_freq(self, freq_map):
        freq_list = []
        for char in freq_map:
            _main = Huff_Node(char, freq_map[char])
            heapq.heappush(freq_list, _main)
        return freq_list

    def huff_tree(self, freq_list):
        if len(freq_list) == 1:
            _main = heapq.heappop(freq_list)
            parent = Huff_Node(None, _main.freq)
            parent.left = _main
            heapq.heappush(freq_list, parent)


        while len(freq_list) > 1:
            left = heapq.heappop(freq_list)
            right = heapq.heappop(freq_list)
            freq_sum = left.freq + right.freq
            parent = Huff_Node(None, freq_sum)
            parent.left = left
            parent.right = right
            heapq.heappush(freq_list, parent)
        return freq_list

    def clean_nodes(self, tree, code):
        huff_code = {}

        if not tree:
            return {}

        if tree.char is not None:
            huff_code[tree.char] = code
        huff_code.update(self.clean_nodes(tree.left, code + "0"))
        huff_code.update(self.clean_nodes(tree.right, code + "1"))
        return huff_code

    def build_codes(self, tree):
        if not tree.left:
            if tree.right is None:
                return {tree.char:'0'}
        return self.clean_nodes(tree, "")

    def huffman_encoding(self, text):
        assert(text)

        list_of_freq = self.list_of_frequency(text)
        min_heap = self.sort_freq(list_of_freq)
        huff_map = self.huff_tree(min_heap)
        tree = heapq.heappop(huff_map)


        huff_code = self.build_codes(tree)
        data = ""
        for char in text:
            data += huff_code[char]
        return data, tree

    def huffman_decoding(self, data, tree):

        decoded = ""
        assert(data)
        temp = tree

        for char in data:
            if char == '0':
                temp = temp.left
            else:
                temp = temp.right
                
            if temp.char is not None:
                decoded += temp.char
                temp = tree

        return decoded  


if __name__ == "__main__":
    Huffman_Code = Huffman_Code()

    a_great_sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman_Code.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman_Code.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    
    a_great_sentence = "A"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman_Code.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman_Code.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    a_great_sentence = "AAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman_Code.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman_Code.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


import sys

import heapq



class Huff_Node(object):
    def __init__(self, value,frequency):
        self.value = value
        self.left= None
        self.right = None
        self.frequency = frequency

    def __str__(self):
        return str(self.value) +" "+ str(self.frequency)


    def __lt__(self,other):
        return self.frequency < other.frequency
        


# build a frequency function to get the frequency 
# of each unique character in the  string
def get_frequencies( data):
    frequency = {}
    for element in data:
        if element not in frequency:
            frequency[element] = 1
        else:
            frequency[element] += 1

    # creat a sorted list key, freq tuple pairs
    freq_sorted = sorted(zip(frequency.keys(), frequency.values() ))

    for i in range(len(freq_sorted)):

        value = freq_sorted[i][0]
        freq = freq_sorted[i][1]

        freq_sorted[i] = Huff_Node(value,freq)
    
    return freq_sorted
        


def huffman_tree(data):
    heap = get_frequencies(data)

    heapq.heapify(heap)

    while len(heap) != 1:
        Z = Huff_Node(None,None)
        lft = heapq.heappop(heap)
        Z.left = lft
        rgt = heapq.heappop(heap)
        Z.right = rgt
        Z.frequency = lft.frequency + rgt.frequency

        heapq.heappush(heap,Z)

    return heap





def Huffcode_table(tree):
    code = {}

    def getCode(hNode, currentCode=""):
        if hNode == None:
            return
        if hNode.left == None and hNode.right == None:
            code[hNode.value] = currentCode
        getCode(hNode.left, currentCode + "0")
        getCode(hNode.right, currentCode + "1")

    getCode(tree[0])

    return code







def huffman_encoding(data):
    
    if len(get_frequencies(data)) == 1:
        return "0"*len(data)
    
    huffcode = ""
    tree = huffman_tree(data)

    table = Huffcode_table(tree)

    for element in data:
        huffcode += table[element]
    
    return huffcode, huffman_tree(data)



def huffman_decoding(data,tree):
    
    if len(get_frequencies(data)) == 1:
        return len(data) * str(tree.value)
    decode = ""
    n = len(data)

    count = 0

    while count < n:
        current = tree[0]
        while current.left != None and current.right != None:
            if data[count] == "0":
                current = current.left
            else:
                current = current.right
            count += 1
        decode += current.value

    return decode





if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
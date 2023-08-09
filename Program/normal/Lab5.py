import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")
def encode(text, huffman):
    map = {}
    def traverse_tree(node, code=''):
        if node.left:
            traverse_tree(node.left, code + '0')
        if node.right:
            traverse_tree(node.right, code + '1')
        if not node.left and not node.right:
            map[node.symbol] = code
    traverse_tree(huffman)

    encoded = ''
    for char in text:
        encoded += map[char]
    return encoded

def decode(encoded, huffman):
    text = ''
    current_node = huffman
    for bit in encoded:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            text += current_node.symbol
            current_node = huffman
    return text

chars = input("").split(' ') # a b c d e f g
freq = [int(i) for i in input("").split(' ')]  # 10 15 12 3 4 13 1

nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = '0'
    right.huff = '1'
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)
printNodes(nodes[0])

huffman_tree = nodes[0]

decoded = decode(input("Enter the decode text: "), huffman_tree)
print("Decoded text:", decoded)
encoded = encode(input("Enter text to encode text: "), huffman_tree)
print("Encoded binary text:", encoded)


"""
a b c d e f g
10 15 12 3 4 13 1
c -> 00
f -> 01
b -> 10
e -> 1100
g -> 11010
d -> 11011
a -> 111
Enter the decode text: 11001101011010
Decoded text: egg
Enter text to encode text: dad
Encoded binary text: 1101111111011
"""
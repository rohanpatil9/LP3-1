# Use string : BCAADDDCCACACAC for testing

class NodeTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def childrens(self):
        return self.left, self.right

def huffman_coding(node, string=''):
    if type(node) is str:
        return {node: string}
    (l, r) = node.childrens()
    d = dict()
    d.update(huffman_coding(l, string+'0'))
    d.update(huffman_coding(r, string+'1'))
    return d


if __name__ == '__main__':
    string = input("Enter a string: ")
    frequency = {}
    for character in string:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    frequency = sorted(frequency.items(), key = lambda x : x[1], reverse = True)
    nodes = frequency


    while len(nodes) > 1:
        (key1 , c1) = nodes[-1]
        (key2 , c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1+c2))
        nodes = sorted(nodes, key = lambda x:x[1], reverse=True)

    output_code = huffman_coding(nodes[0][0])
    print('Characters\t | Frequency \t | Huffman Code')
    print('==============================================')
    for (char, freq) in frequency:
        print( char, '\t\t | ', freq, '\t\t | ', output_code[char])

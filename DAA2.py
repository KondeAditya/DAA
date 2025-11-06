def build_tree(freq):
    nodes = [[freq[ch], ch] for ch in freq]     # each node = [weight, data]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x[0])
        left = nodes.pop(0)
        right = nodes.pop(0)
        new = [left[0] + right[0], [left, right]]  # merge
        nodes.append(new)
    return nodes[0]


def assign(node, code="", table={}):
    if isinstance(node[1], str):         # leaf
        table[node[1]] = code
    else:
        left, right = node[1]
        assign(left, code+"0", table)
        assign(right, code+"1", table)
    return table


def huffman(text):
    # freq count
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1

    # build + assign
    root = build_tree(freq)
    codes = assign(root)

    # print
    for ch in sorted(codes):
        print(ch, ":", codes[ch])


txt = "abbbbbbcccddddddddee"
huffman(txt)

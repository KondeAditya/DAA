import heapq
import itertools

def build_huffman_tree(freq):
    heap = []
    counter = itertools.count()  # unique sequence count
    for ch, weight in freq.items():
        heap.append([weight, next(counter), [ch]])  # add counter as second element
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        combined_weight = low[0] + high[0]
        combined_node = [low[2], high[2]]
        heapq.heappush(heap, [combined_weight, next(counter), combined_node])

    return heap[0]

def assign_codes(node, prefix="", codebook={}):
    # node is [char] for leaf, or [left, right] for internal node
    if len(node) == 1 and isinstance(node[0], str):
        codebook[node[0]] = prefix
    else:
        assign_codes(node[0], prefix + "0", codebook)
        assign_codes(node[1], prefix + "1", codebook)
    return codebook

def huff_en(txt):
    freq = {}
    for c in txt:
        freq[c] = freq.get(c, 0) + 1

    root = build_huffman_tree(freq)
    codes = assign_codes(root[2])  # Note: root[2] because of tie-breaker

    print("Huffman Codes:")
    for ch in sorted(codes):
        print(f"{ch}: {codes[ch]}")

txt="abbbbbbcccddddddddee"
huff_en(txt)
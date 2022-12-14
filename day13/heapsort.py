from typing import *

def left_child(n: int) -> int:
    """
    0-indexed heap:
    index left_child = 2i + 1
    index right_child = 2i + 2
    """
    return (2 * n) + 1

def swap(heap: List[int], i: int, j: int) -> None:
    heap[i], heap[j] = heap[j], heap[i]

def bubble_down(heap: List[int], index: int, compare) -> None:
    """
    Compare the value at the current index
    to that of its left and right children.

    If the value doesn't dominate its two child nodes,
    swap it with the min of the three nodes,
    then make a recursive call with the new index of
    the original root.

    Keep repeating until either the original root reaches a
    point in the tree where it dominates its children.
    """
    min_index = index
    left_child_index = left_child(index)
    for i in range(2):
        # As we approach the bottom of the tree, our node may not have children.
        if left_child_index + i < len(heap):
            if compare(heap[min_index], heap[left_child_index + i]):
                min_index = left_child_index + i
    if min_index != index:
        swap(heap, index, min_index)
        bubble_down(heap, min_index, compare) 

def make_heap_fast(s: List[int], compare) -> List[int]:
    """
    We know that a heap with one element is a valid min/max heap.
    We also know that a balanced binary tree of n nodes has n / 2 leaf nodes.
    This means we can make use of bubble_down to move the n / 2 nodes with children
    to their correct position in the heap.
    It turns out that this takes O(n) time rather than O(n log n).
    See Skiena p.122 for an explanation.
    """
    n = len(s)
    for i in range(n // 2, -1, -1):
        bubble_down(s, i, compare)
    return s

def extract_min(heap: List[int], compare) -> int:
    """
    The root is always the min of a min-heap.

    After extracting the min, we replace the root
    with the final element of the arrray.

    Then because this may not result in a min-heap, we
    must move the new root to a position in the tree
    so that we get a min-heap.

    When we next call extract_min, we know that the root
    is the min.
    """
    min_val = -1
    if len(heap) <= 0:
        print("Warning: empty priority queue.\n")
    elif len(heap) == 1:
        # Adding this case prevents index out of bounds
        # Consider when heap = [1]
        # heap.pop() will return 1
        # then heap will be [], which has no 0th index
        min_val = heap[0]
        heap.pop()
    else:
        min_val = heap[0]
        heap[0] = heap.pop()
        bubble_down(heap, 0, compare)
    return min_val
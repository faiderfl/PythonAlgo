
from src.BinarySearch import binary_search


def test_binary_search():
    sorted_list = [1,3,4,5,7,8,12,16]
    index =7
    assert binary_search(sorted_list, index)==4

from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    dt = defaultdict(int)
    for ch in s:
        dt[ch] +=1
    return dt
    
def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    dt = defaultdict(list)
    for lst in nums:
        key = lst[0]
        lst.remove(key)
        dt[key].extend(lst)
    return dt


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))

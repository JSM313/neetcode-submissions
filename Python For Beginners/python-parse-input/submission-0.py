from typing import List

def read_integers() -> List[int]:
    raw_tokens = input().split(",")
    new_list = []
    for token in raw_tokens:
        new_list.append(int(token))
    return new_list

print(read_integers())
print(read_integers())
print(read_integers())

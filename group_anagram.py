import collections
import re
from typing import List

def groupAnagram(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))
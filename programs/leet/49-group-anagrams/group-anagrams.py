# Leetcode Problem 49
# "Group Anagrams"
# Solution by Quinn Johnson 7/15/23

# Implementation

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groupings = []
    anagrams = {}

    # Hashmap solution
    # 1. Create map that stores a unique sorted anagram and index
    # 2. The index will point to the grouping the word should be in
    # 3. This will require a string sort on every word
    # This may be fast enough as the maximum is 100 characters per word

    index = 0
    for i in range(len(strs)):
        sortedWord = "".join(sorted(strs[i]))
        if (sortedWord in anagrams):
            groupings[anagrams[sortedWord]].append(strs[i])
            continue
        anagrams[sortedWord] = index
        groupings.append([strs[i]])
        index += 1

    return groupings



# Acceptance Tests
#assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]


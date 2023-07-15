# Leetcode Problem 242
# "Valid Anagram"
# Solution by Quinn Johnson 7/15/23

def adjustFrequency(s: str, frequency: dict, operation: int) -> dict:
    for c in s:
        if (c in frequency):
            frequency[c] += 1 * operation
            continue
        frequency[c] = 1
    return frequency


def isAnagram(s: str, t: str) -> bool:
    characterFrequency = {}

    characterFrequency = adjustFrequency(s, characterFrequency, 1)
    
    characterFrequency = adjustFrequency(t, characterFrequency, -1)


    for frequency in characterFrequency:
        if characterFrequency[frequency] > 0:
            return False
    
    return True

    # of course return sorted(s) == sorted(t) will work as well
    # frequency lists are in O(n) while sorted will run quick in O(n log n)


# Acceptance Tests
assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
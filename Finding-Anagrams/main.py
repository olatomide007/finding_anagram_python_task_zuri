# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    
    # [assignment] Add your code here
    sorted_word = sorted(word.replace(" ","").lower())
    sorted_anagram = sorted(anagram.replace(" ", "").lower())
    #print(sorted_word)
    #print(sorted_anagram)
    if len(sorted_word) == len(sorted_anagram):
        if sorted_word == sorted_anagram:
            return True
    else:
        return False

print(find_anagram("Dormitory","Dirty Room")) # arranging the two words will always be te same ence word and anagram
print(find_anagram("Below","elbow"))# case insensive
print(find_anagram("The country side","No City Dust Here"))#more than a word

# An Anagram Detection Example

def anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

#     check if the len are the same

    if len(s1) != len(s2):
         return False

    # create a dictonary
    letter = {}


    for k in s1:
        if k in letter:
            letter[k] +=1
        else:
            letter[k] = 1

    for k in s2:
        if k in letter:
            letter[k] -=1
        else:
            letter[k] = 1


    for k in letter:
        if letter[k] != 0:
            return False
    return True



anagram("dog","god")
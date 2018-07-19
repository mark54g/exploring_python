def LetterChanges(word): 

    alpha = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    newword = []
    for letter in word:
        if letter.isalpha():
            if letter in alpha:
                if letter == 'z':
                    letter = 'a'
                else:
                    newindex = alpha.index(letter) + 1
                    letter = alpha[newindex]
                if letter in vowels:
                    newword.append(letter.upper())
                else:
                    newword.append(letter)
        else:
            newword.append(letter)       
    newword = ''.join(map(str, newword))
    return newword
    
print LetterChanges(input())

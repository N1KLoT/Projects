'''
Created on 14.08.2014

@author: Thomas
'''
'''
Rules:
    For words that begin with consonant sounds, the initial consonant or consonant cluster is moved to the end of the word, 
    and "ay" (some people just add "a") is added, as in the following examples:
    "happy" -> "appyhay"
    "duck" -> "uckday"
    "glove" -> "oveglay"
    
    For words that begin with vowel sounds or silent letter, you just add "way" (or "wa") to the end. Examples are:
    "egg" -> "eggway"
    "inbox" -> "inboxway"
    "eight" -> "eightway"
'''

def main():
    input_string = input("Word to translate to pig tail: ")
    vowels = "aeiou";
    pig_tail = "";
    if input_string[0] in vowels:
        # starts with vowel
        pig_tail = input_string + "way"
    else:
        #starts with consonant
        i = 1
        while input_string[i] not in vowels:
            i += 1
        pig_tail = input_string[i:] + input_string[:i] + "ay"
            
    
    print(input_string + " translated to pig tail is " + pig_tail)

if __name__ == "__main__":
    main()
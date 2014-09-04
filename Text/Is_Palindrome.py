'''
Created on 17.08.2014

@author: Thomas
'''

def main():
    input_string = input("Enter word to check if palindrome: ")
    is_palindrome = True
    half_input = input_string[0:int((len(input_string)+1)/2)]
    for i, c in enumerate(half_input):
        if c != input_string[-(i+1)]:
            is_palindrome = False
            exit
    
    print(is_palindrome)

if __name__ == '__main__':
    main()
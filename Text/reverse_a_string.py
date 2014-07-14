'''
Created on Jul 14, 2014

@author: thomasknell
'''

def main():
    input_string = input("string to reverse: ")
    reversed_string = ""
    for i in range(1, len(input_string) + 1):
        reversed_string += input_string[len(input_string) - i]
    print(input_string + " revered is " + reversed_string)

if __name__ == "__main__":
    main()

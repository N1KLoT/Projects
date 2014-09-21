'''
Created on 21.09.2014

@author: Thomas
'''

def main():
    print("Collatz Conjecture")
    input_number = -1
    
    while input_number <= 1:
        input_string = input("Input number: ")
        if input_string.isdigit():
            input_number = int(input_string)
        if (not input_string.isdigit()) or (input_number <= 1):
            print("Please enter number bigger than 1")
    
    steps = 0
    n = input_number
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = n*3 + 1
        steps += 1
    
    print("It takes " + str(steps) + " steps for " + str(input_number) + " to reach 1.")

if __name__ == '__main__':
    main()
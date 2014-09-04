'''
Created on 17.08.2014

@author: Thomas
'''
def main():
    input_string = input("String to count vowels: ")
    counter = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    for c in input_string:
        if c in counter:
            counter[c] += 1
            
    for k, v in counter.items():
        print("Numbers of " + k +"'s in string: " + str(v))

if __name__ == '__main__':
    main()

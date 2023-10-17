#!/usr/bin/python3
def hashing_by_division(k, m):
    return k % m


def main():
    dictionary = {
        'a' : 1,
        'b' : 2,
        'c' : 'Addis ababa',
        'd' : True
    }
    

    print(dictionary)

    #insert
    dictionary['e'] = False
    print(dictionary)

    #delete
    del dictionary['e']
    print(dictionary)

    #search
    print(dictionary['c'])

    #key = 50, table = 13
    k = 50
    m = 13
    print(f'hash of 50 with table size 13 --> {hashing_by_division(k, m)}')

main()
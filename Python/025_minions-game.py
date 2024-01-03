def minion_game(string):
    vowels=[ "a", "e", "i", "o", "u" ]

    stuart=0
    kevin=0
    i=0
    for a in s:
        if a.isalpha():
            if a.lower() in vowels: 
                kevin=kevin+len(s)-i
            else:
                stuart=stuart+len(s)-i
        i=i+1
    if stuart > kevin :
        print(f'Stuart {stuart}')
    elif stuart == kevin:
        print("Draw")
    else:
        print(f'Kevin {kevin}')

if __name__ == '__main__':
    s = input()
    minion_game(s)
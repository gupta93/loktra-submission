
def getHashString():

    expected = 930846109532517
    letters  ="acdegilmnoprstuw"

    ans = ''

    while True:

        if expected==7:
            break
        for i in range(0,16):
            if (expected-i)%37==0:
                ans += letters[i]
                expected -=i
                expected/=37
                break


    print ans[::-1]


if __name__=='__main__':
    getHashString()
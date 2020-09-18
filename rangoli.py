def print_rangoli(size):
    fim = ""
    fill = (size+(size-1))*2-1
    letters = "abcdefghijklmnopqrstuvwxyz"[0:size]

    cont = 0
    back = False
    for x in (letters[::-1]+letters[1:]):
        if cont<size and not back:
            cont+=1
        else:
            back = True
            cont-=1
        msg = letters[0:1]
        for y in (letters[1:cont]):
            msg += "-"+y
        
        msg += (msg[::-1])[1::]
        print(msg.center(fill,"-"))
def print_rangoli(size):
    fill = (size+(size-1))*2-1
    letters = "abcdefghijklmnopqrstuvwxyz"[0:size]

    cont = 0
    back = False
    
    reverse = (letters[::-1]+letters[1:])
    for x in (reverse):
        if cont<size and not back:
            cont+=1
        else:
            back = True
            cont-=1
        msg = reverse[0:1]
        for y in (reverse[1:cont]):
            msg += "-"+y
        
        msg += (msg[::-1])[1::]
        print(msg.center(fill,"-"))
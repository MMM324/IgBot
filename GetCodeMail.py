string = '<h5 class="modal-title fw-normal" id="mensaje-modal-1656906168853-label">326718 is your Instagram code</h5>'
codigo = ""
def cutString(str, charCut):
    newList = []
    newList2 = list(str)
    for x in range(len(string)):
        newList.append(string[x])
        if(string[x] == charCut):
            break
    for x in newList:
        newList2.remove(x)
    return newList2
for num in cutString(cutString(string,">"),"<"):
    if(ord(num) >= 48 and ord(num) <= 57):
        codigo += str(num)
print(codigo) 

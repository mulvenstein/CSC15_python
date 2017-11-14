#author tom mulvey
#date 11 14
# ves .01
#purpose : decrompress an encoded strings of multiple 1 and 0

from PIL import Image

def rle_decompress(in_rle):
    output = ""
    rep_str = "" #accumalting string for * characters
    state = "" #either non rep or rep state

    for char in in_rle :
        if char == "*" : #sets state to repete mode
            state = "rep"
        elif char == " ": #sets state to non repeat, also prints the rep_str if there is one
            state = "nonrep"
            output= output + decomp_string(rep_str)
            rep_str = "" #resets rep_str to empty for next rep set
        else :
            if state == "nonrep": #non rep state. accumulate
                output += char
            else : #rep state
                rep_str += char
 
    return output

def decomp_string(rep_str):
    if rep_str == "": #if there is no string, return nothing!
        return ""
    else :
        new_str = rep_str[:-1] #splices last term off so we know how long to loop
        loop = int(new_str)
        new_str = loop * rep_str[-1]
        return new_str

def main():
    ifile = open("cheesy.rle")
    data = ifile.read()
    pix = rle_decompress(data)
    spl = list(pix)
    pl = list(map(lambda a: 1 if a == '1' else 0, spl))
    i = Image.new("1", (910,912))
    i.putdata(pl)
    i.save("test.png")
    return

###
main()

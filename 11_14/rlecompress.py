#author tom mulvey
#date 11 14
# ves .01
#purpose : compress long string
def rle_compress(in_data):
    # Complete this function
    if in_data == "" :
        ans = ""
    else :
        last_c = in_data[0]
        max_i = len(in_data)
        i = 1
        while i < max_i and last_c == in_data[i] :
            i = i + 1
        if i > 3:
            string = "*"+str(i)+last_c + " "
        else :
            string = i*last_c 
        ans = string + rle_compress(in_data[i:])
    return ans.rstrip()

def main():
    sample1 = "00011111000000111"
    expected1 = "000*51 *60 111"

    sample2 = "11111110111111"
    expected2 = "*71 0*61"
    print(rle_compress(sample1), rle_compress(sample2))
    if rle_compress(sample1) == expected1:
        print("Program has passed test 1.")
    else:
        print("Program has failed test 1.")

    if rle_compress(sample2) == expected2:
        print("Program has passed test 2.")
    else:
        print("Program has failed test 2.")

    return
###
main()

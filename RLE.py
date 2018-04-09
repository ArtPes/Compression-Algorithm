def RLE_encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
                # print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        try:
            entry = (character, count)
            lst.append(entry)
            return lst
        except Exception as e:
            print("Exception encountered {e}".format(e=e))
            return e


def RLE_decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q



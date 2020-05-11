def unpack(input_tuple):
    # your code here
    unpacked = list()
    for i in input_tuple:
        if isinstance(i, tuple):
            for j in i:
                unpacked.append(j)
        else:
            unpacked.append(i)
    return tuple(unpacked)

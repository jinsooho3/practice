for index in range(1, 60):
    value = str(index)
    flag = False
    msg = ""

    for index_char in value:
        if index_char == "3" or index_char == "6" or index_char == "9":
            msg += "clap "
            flag = True
    
    if flag:
        print(msg)
    else:
        print(index)
def balance(str, open_char ='(', close_char =')' ) :
    ''' returns str after unmatched opening and closing charaters removed
        any { } < > open close single char supported. 
        More than 1 char brackets such as /* */ not supported'''
    copystr=''
    unmatched_open_brackets = []
    # at end of this loop, all unmatched closing char will be absent in copystr
    # and all unmatched opening char positions in copystr will be present in the unmatched_open_brackets.
    indx = 0
    for c in str:
        if c == open_char :
            unmatched_open_brackets.append(indx)
        elif c == close_char :
            if len(unmatched_open_brackets) > 0 : 
                unmatched_open_brackets.pop()
            else : # un matched close bracket char
               continue # igore and move on to next char
        #copy as long as not a non matching char:
        copystr += c
        indx += 1
    #print ( copystr)        
    #print (unmatched_open_brackets)
    if len(unmatched_open_brackets) == 0 :
        return copystr
    else :
       # The next 4 lines code below is equal to next three lines in comment:
       #  str = ""
       #  for i  in range(0,len(unmatched_open_brackets) ) :
       #      if i not in unmatched_open_brackets : str += copystr[i]
        str = copystr[0:unmatched_open_brackets[0]]
        for i  in range(0,len(unmatched_open_brackets)-1) :
            str += copystr[unmatched_open_brackets[i]+1:unmatched_open_brackets[i+1]]
        str += copystr[unmatched_open_brackets[-1]+1:len(copystr)]
        return str

print (" Reuslt = " + balance("()))(a(b)c)))(((d)(()("))
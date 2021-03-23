def num2xlcol(col_num):
    """ numtxlcol(col_num)
    col_num -  integer greater than zero
    returns string corresponding to MS excel column""" 
    n=1
    while col_num>26*(26**n-1)//25:
        n+=1                            
    base_26 =['']*n                     
    tmp_var=-1+col_num-26*(26**(n-1)-1)//25 
    for k in range(1,n+1):
        divisor = 26**(n-k)
        base_26[k-1]= chr(65 + tmp_var//divisor)
        tmp_var = tmp_var % divisor
    return ''.join(base_26)

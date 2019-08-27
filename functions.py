import primefac
import numpy as np
import pandas as pd
import random

def table_stats(max_val, prime_factors=True):
    """Return some statistics on a pythagoras table of size max_val
    
    Returns a tuple with two dictioaries.
    Count the number of occurences of number is a pythagoras table of size max_val.
    This is returnes as a dictionary with the number as key and its occurence as value.
    Also return a the prime factors of the numbers as a dictionary, whem prime_factors
    is True. Otherwise returns an empty dictionary.
    """
    count_num = { }
    prime_fac = { }

    # initialize count of occurrences of a certain number
    for i in range(1, max_val*max_val+1):
        count_num[i] = 0;

    # calculate the pythagorean square and count occurrence of each number
    for i in range(1, max_val+1):
        for j in range(1, max_val+1):
            count_num[i*j] += 1

    # make a dictionary of prime factors of all the numbers
    if(prime_factors):
        for tuple in count_num.items():
            prime_fac[tuple[0]] = primefac.factorint(tuple[0]) 
    
    return (count_num, prime_fac)

def gen_table(max_val):
    """Return Pythagoras table of size max_val as a 2D numpy array."""
    table = np.zeros((max_val, max_val), dtype=int)
    
    for i in range(1, max_val+1):
        for j in range(1, max_val+1):
            table[i-1, j-1] = i*j
            
    return table

def gen_dataframe(max_val, drop_out=0):
    """Return Pythagoras table of size max_val as a Pandas dataframe
    
    Optional parameter drop_ouz (0 to 1) to leave out a fraction of elements."""
    np_arr = gen_table(max_val)
    df = pd.DataFrame(data=np_arr[0:,0:],
                      index=np_arr[0:,0],
                      columns=np_arr[0,0:])
    
    if(drop_out > 0):
        for i in range(2, max_val+1):
            for j in range(2, max_val+1):
                if(random.random() < drop_out):
                    df.loc[i, j] = np.nan
        
    return(df)

def write_html(file_name, max_val, drop_out=0):
    """Write Pythagoras table of size max_val as HTML table to file file_name."""
    df = gen_dataframe(max_val, drop_out)

    with open(file_name, "w") as fo:
        df.to_html(fo, na_rep="", float_format=lambda x : "{:.0f}".format(x).replace("nan", ""))
    return()
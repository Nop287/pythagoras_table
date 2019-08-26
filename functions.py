import primefac
import numpy as np
import pandas as pd

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

def gen_dataframe(max_val):
    """Return Pythagoras table of size max_val as a Pandas dataframe"""
    np_arr = gen_table(10)
    df = pd.DataFrame(data=np_arr[0:,0:],
                      index=np_arr[0:,0],
                      columns=np_arr[0,0:])
    return(df)
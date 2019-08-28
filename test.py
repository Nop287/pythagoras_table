from functions import table_stats, gen_table, gen_dataframe, write_html
import pandas as pd

write_html("test.html", 10, 0.1)

(count_num, prime_fac) = table_stats(100)

# make a list of items in the dictionary sorted by occurence
list_of_items = sorted(count_num.items(), key=lambda x : x[1])

# print the numbers, their occurrence (including 0 occurrences) and their prime factors
for tuple in list_of_items:        
    print(tuple[0], " : ", tuple[1], end='')
    print(" : ", prime_fac[tuple[0]])

count_hist = { }

# calculate a histogram: How many numbers did occur a certain amount of times?
for tuple in list_of_items:
    if tuple[1] in count_hist.keys():
        count_hist[tuple[1]] += 1
    else:
        count_hist[tuple[1]] = 1
        
# print the histogram
print(count_hist)
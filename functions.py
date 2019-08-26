import primefac

# How big should the pythagorean table be?
max_val = 10

count_num = { }
prime_fac = { }

# initialize count of occurrences of a certain number
for i in range(1, max_val*max_val+1):
    count_num[i] = 0;

# calculate the pythagorean square and count occurrence of each number
for i in range(1, max_val+1):
    for j in range(1, max_val+1):
        count_num[i*j] += 1

# make a list of items in the dictionary sorted by occurence
list_of_items = sorted(count_num.items(), key=lambda x : x[1])

# make a dictionary of prime factors of all the numbers
for tuple in list_of_items:
    prime_fac[tuple[0]] = primefac.factorint(tuple[0]) 
    

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
    
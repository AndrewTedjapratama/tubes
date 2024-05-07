import os, time

def lcg(seed, a, c, m):
    # linear congruential generator
    x = seed
    while True:
        x = (a * x + c) % m
        yield x

def random_number_generator():
    # Generate a random number
    m = 2 ** 31                     
    a = 10012893123123              
    c = 0                           
    seed_random = int(os.getpid() + time.time()) # random seed per time
    gen_rand = lcg(seed_random, a, c, m)
    rand = next(gen_rand) / m # random number [0,1]
    return rand



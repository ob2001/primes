import numpy as np
import sys

# np.set_printoptions(threshold=sys.maxsize)

def calc(x, term = True, dbg = False):
    sqrt = np.sqrt(x)
    arr = np.arange(2, int(sqrt + 1) if term else x)
    primes = []
    
    while True:
        n = arr[0]
        if dbg:
            print(n)

        if term:
            k = x/n
            if k.is_integer():
                primes.append(n)
                return np.array(primes)
        elif n > sqrt:
            return np.concatenate((np.array(primes), arr))
        
        if len(arr) > 1:
            primes.append(n)
            arr = arr[arr % n != 0]
        else:
            primes.append(n)
            return (np.array(primes), None) if term else np.array(primes)

if __name__ == "__main__":
    mode = {"s": "single", "r": "range"} # "s" for single integer, "r" to find primes up to given integer
    mode = mode[input("Mode select: ")]

    dbg = True

    match mode:
        case "single":
            x = int(input("What number would you like to check?: "))
            primes, n = calc(x, dbg = dbg)
            print(f"{x} is prime!") if n == None else print(f"{x} is divisible by {n}")
        case "range":
            x = int(input("To what upper bound?: "))
            primes = calc(x, False, dbg = dbg)
            print(f"Primes found: {primes}\n\nNum primes found: {len(primes)}")

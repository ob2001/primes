from math import sqrt

def calc(x, term = True):
    arr = [i for i in range(2, int(sqrt(x)) + 1 if term else x)]
    i = 1
    primes = []
    
    while True:
        n = arr[0]
        if term:
            k = x/n
            if k.is_integer():
                primes.append(n)
                return primes, n
        if len(arr) > 1:
            primes.append(n)
            arr = [arr[i] for i in range(1, len(arr)) if arr[i] % n != 0]
            i += 1
        else:
            primes.append(n)
            return primes, None

if __name__ == "__main__":
    mode = {"s": "single", "r": "range"} # "s" for single integer, "r" to find primes up to given integer
    mode = mode[input("Mode select: ")]

    match mode:
        case "single":
            x = int(input("What number would you like to check?: "))
            primes, n = calc(x)
            print(f"{x} is prime!") if n == None else print(f"{x} is divisible by {n}")
        case "range":
            x = int(input("To what upper bound?: "))
            primes, _ = calc(x, False)
            print(f"Primes found: {primes}\n\nNum primes found: {len(primes)}")

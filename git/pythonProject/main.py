


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return a * b // gcd(a, b)
# Calculates the number of coprimes between 1 and n.
def phi(n):
    num_coprimes = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            num_coprimes += 1
    return num_coprimes


def main():
    print(gcd(11, 3))

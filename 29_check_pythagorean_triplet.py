# Task 29: Check Pythagorean Triplet
def is_pythagorean_triplet(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

if __name__ == "__main__":
    a, b, c = map(int, input("Enter three numbers: ").split())
    print("Pythagorean triplet:" if is_pythagorean_triplet(a, b, c) else "Not a triplet")

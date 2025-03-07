def is_prime(num:int) -> bool:
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

i = int(input())

print(is_prime(i))
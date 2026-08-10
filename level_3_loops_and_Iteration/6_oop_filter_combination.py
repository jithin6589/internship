def find_primes():
    prime_count = 0
    for number in range(2, 21):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count = prime_count + 1
            if prime_count % 2 != 0:
                print(number)
def main():
    find_primes()
main()
def print_multiplication_table(n) :
    for i in range(1,n+1):
        for j in range(1,11):
            print(f"{i} * {j} = {i*j}", end = " ")
        print("\n")

def main():
    n=int(input("enter the number of rows"))
    print_multiplication_table(n)
main()

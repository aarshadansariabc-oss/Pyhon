def isPrime(n):
    is_prime = True
    if n <=1 :
        print("Nither prime nor Composit")
    else:
        for i in range (2, n):
            if n % i == 0:
                is_prime = False
        if is_prime :
            print("Its a Prime number")
        else:
            print("Not a prime number")


number = int(input("Enter your Number : "))
isPrime(n = number)

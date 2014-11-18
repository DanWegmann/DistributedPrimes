import rpyc
c = rpyc.connect("localhost", 12345)
c.root

int main():
    c.root.isPrime(44)

    return 0

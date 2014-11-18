import rpyc
c = rpyc.connect("localhost", 12345)
c.root.isPrime(45)
c.root.isPrime(113)

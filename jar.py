class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * '🍪'


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('Exceed Capacity')
        if self.size + n > self.capacity:
            raise ValueError('Exceed Capacity')
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Less than asked")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    print(jar)


if __name__=="__main__":
    main()


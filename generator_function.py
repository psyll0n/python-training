import time

n = int(input("Please, enter a number to start the countdown: "))

# Sample function using a generator.
def countdown(n):
    print("Starting to count down from", n, "...")
    while n > 0:
        yield n
        n -= 1


# Create the generator.

c = countdown(n)

for i in range(0, n):
    print(next(c))
    time.sleep(1)
print("Done!")

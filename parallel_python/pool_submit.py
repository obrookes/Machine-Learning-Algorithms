import os
import time
from concurrent.futures import ProcessPoolExecutor

def slow_function(nsecs):
    """
    Function that sleeps for 'nsecs' seconds, returning
    the number of seconds that it slept
    """

    print(f"Process {os.getpid()} going to sleep for {nsecs} second(s)")

    # use the time.sleep function to sleep for nsecs seconds
    time.sleep(nsecs)

    print(f"Process {os.getpid()} waking up")

    return nsecs

def slow_add(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then returns the sum of x and y
    """
    print(f"Process {os.getpid()} going to sleep for {nsecs} second(s)")

    time.sleep(nsecs)

    print(f"Process {os.getpid()} waking up")

    return x + y

if __name__ == "__main__":
    print(f"Master process is PID {os.getpid()}")

    with ProcessPoolExecutor() as pool:
        r = pool.submit(slow_add, 2, 3, 7)
        r = pool.submit(slow_add, 2, 30, 76)
        # Useful type checker...
        print(type(r))

    print(f"Result is {r.result()}")
import time
import sys
from concurrent.futures import ProcessPoolExecutor

def slow_add(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then returns the sum of x and y
    """
    time.sleep(nsecs)
    return x + y

def slow_diff(nsecs, x, y):
    """
    Function that sleeps for 'nsecs' seconds, and
    then retruns the difference of x and y
    """
    time.sleep(nsecs)
    return x - y

def broken_function(nsecs):
    """Function that deliberately raises an AssertationError"""
    time.sleep(nsecs)
    raise ValueError("Called broken function")

if __name__ == "__main__":

    futures = []

    with ProcessPoolExecutor(max_workers=int(sys.argv[1])) as pool:
        futures.append(pool.submit(slow_add, 3.1, 6, 7))
        futures.append(pool.submit(slow_diff, 2.1, 5, 2))
        futures.append(pool.submit(slow_add, 1.1, 8, 1))
        futures.append(pool.submit(slow_diff, 5.1, 9, 2))
        futures.append(pool.submit(broken_function, 4.1))

        while True:
            all_finished = True

            print("\nHave the workers finished?")

            for i, future in enumerate(futures):
                if future.done():
                    print(f"Task {i} has finished")
                else:
                    all_finished = False
                    print(f"Task {i} is running...")

            if all_finished:
                break

            time.sleep(1)

        print("\nHere are the results.")

        for i, future in enumerate(futures):
            if future.exception() is None:
                print(f"Task {i} was successful. Result is {future.result()}")
            else:
                print(f"Task {i} failed!")
                e = future.exception()
                print(f"    Error = {type(e)} : {e}")
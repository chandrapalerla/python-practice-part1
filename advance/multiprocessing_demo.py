import multiprocessing
import time

def square_number():
   for i in range(5):
       print(f"Square of {i} is {i * i}")
       time.sleep(1)

def cube_number():
   for i in range(5):
       print(f"Cube of {i} is {i * i * i}")
       time.sleep(1.5)

if __name__ == "__main__":
    ## Create processes

    process1 = multiprocessing.Process(target=square_number)
    process2 = multiprocessing.Process(target=cube_number)
    t = time.time()

    ## Start processes
    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(f"Total time taken: {time.time() - t} seconds")



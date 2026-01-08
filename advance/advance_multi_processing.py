from concurrent.futures import ProcessPoolExecutor
import time

def square_number(n):
    time.sleep(1)
    return f"Square of {n} is {n * n}" 

numbers = [1, 2, 3, 4, 5,6,7,8,9,10,0,1,2,3]
if __name__ == "__main__":
   
    with ProcessPoolExecutor(max_workers=3) as executor:
        start_time = time.time()
        results = executor.map(square_number, numbers)
        end_time = time.time()

    for result in results:
        print(result)
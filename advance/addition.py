from logger import logging

def add(a,d):
    result = a + d
    logging.debug(f"Adding {a} and {d} to get {result}")
    return result

logging.debug("Adding 10 and 20 to get 30")
add(10,20)
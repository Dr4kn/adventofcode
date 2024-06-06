from aocd import get_data
import hashlib

# part 1
secret_key = get_data(day=4, year=2015)
counter = 0
while True:
    to_hash = secret_key + str(counter)
    hashed = hashlib.md5(to_hash.encode())
    if hashed.hexdigest()[:5] == "00000":
        print(hashed.hexdigest())
        print(counter)
        break
    counter += 1

# part 2
counter = 0
while True:
    to_hash = secret_key + str(counter)
    hashed = hashlib.md5(to_hash.encode())
    if hashed.hexdigest()[:6] == "000000":
        print(hashed.hexdigest())
        print(counter)
        break
    counter += 1
import os

STOP=int(os.environ.get("FIZZBUZZ_STOP",100))

for idx in range(1,STOP+1):
    result = []
    if idx % 3 == 0:
        result.append("fizz")

    if idx % 5 == 0:
        result.append("buzz")
    
    if len(result):
        print(", ".join(result))
    else:
        print(idx)
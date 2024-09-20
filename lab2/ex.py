from datetime import datetime, timedelta
import random

# ex 1
def calculate_call_cost(start: datetime, end: datetime, cost_per_sec: int = 1) -> float:
    cost = (end-start).seconds * cost_per_sec
    if start.weekday() >= 5:
        cost *= 0.8
    return cost

# ex 2
def randint_operations() -> int:
    random.seed(datetime.now().microsecond)
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    if a > 0 and b > 0:
        return a - b
    elif a < 0 and b < 0:
        return a * b
    else:
        return a + b
    
# ex 3
def threesome_sum() -> int:
    r = list(range(102, 200, 3))
    return  r, sum(r)


if __name__ == '__main__':
    print('ex 1:')
    print(calculate_call_cost(datetime.now(), datetime.now() + timedelta(seconds=10)))
    print('ex 2:')
    print(randint_operations())
    print('ex 3:')
    print(*threesome_sum(), sep='\n')
def even_odd(n):
    return bin(n)[-1] == "0" 
    # return str(n)[-1] in ["0","2","4","6","8"]

def average(arr):
    if len(arr) == 0: return 0
    answer = 0
    for i in arr:
        answer += i
    return answer / len(arr)

def max_list(arr):
    if len(arr) == 0: return 0
    return sorted(arr,reverse=True)[0]

def min_list(arr):
    if len(arr) == 0: return 0
    return sorted(arr)[0]
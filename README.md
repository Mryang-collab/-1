# -1
简单的代码
用于存储新学的代码 
复杂度的代码
def Func1(N):
    count = 0
    for i in range(N):
        for j in range(N):
            count += 1
    
    for k in range(2 * N):
        count += 1
    
    M = 10
    while M > 0:
        count += 1
        M -= 1
    
    print(count)

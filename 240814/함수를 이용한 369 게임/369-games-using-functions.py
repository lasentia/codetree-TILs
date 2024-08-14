a, b = list(map(int, input().split()))

def multiple_of_tree(a, b):
    list_a = []
    
    for i in range(a, b+1):
        if i % 3 == 0:
            list_a.append(i)
        
    return list_a

def count_of_num(a, b):
    list_b = []
   
    for i in range(a, b+1):
        if ('3') in str(i) or ('6') in str(i) or ('9') in str(i):
            list_b.append(i)

    return list_b

print(len(set(count_of_num(a, b) + multiple_of_tree(a, b))))
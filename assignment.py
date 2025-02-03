def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
  
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def list_operations(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return (total,maximum,minimum)

def dict_operations(students_dict):
   
    high_scorer = []
    for name, score in students_dict.items():
        if score >80:
            high_scorer.append(name)
    return high_scorer
  

def set_operations(list1, list2):
  
    set1 = set(list1)
    set2 = set(list2)
    commmon_elements = set1 & set2
    return commmon_elements

def arithmetic_ops(a, b):
   
    results = {
        'sum': a+b,
        'difference': a-b,
        'product': a*b,
        'quotient': a/b if b != 0 else None,
  
    }
    return results

def logical_ops(x, y):
   
    result =  {
        'and': x and y,
        'or': x or y,
        'not_x': not x
    }
    return result

def bitwise_ops(a, b):
    result = {
        'and': a & b,  
        'or': a | b,    
        'xor': a ^ b    
    }
    return result
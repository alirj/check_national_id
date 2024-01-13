import re

def valid_n_id(num):
    try: num = f"{int(num):010d}"
    except: return False
    if not re.search(r'^\d{10}$', num):
        return False
    
    check = int(num[-1])
    s = sum([int(num[x]) * (10 - x) for x in range(9)]) % 11
    return (s < 2 and check == s) or (s >= 2 and check + s == 11)


def valid_legal_n_id(num):
    try: num = f"{int(num):011d}"
    except: return False
    if not re.search(r'^\d{11}$', num):
        return False
    check = int(num[-1])
    decimal = int(num[-2]) + 2
    coefficient = [29,27,23,19,17,29,27,23,19,17]
    s = sum([(int(num[x]) + decimal) * coefficient[x] for x in range(10)]) % 11
    if s == 10: s = 0
    return s == check


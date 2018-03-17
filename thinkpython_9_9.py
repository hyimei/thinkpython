def age_group_reversed(gap):
    age_group = []
    age = 1
    her_age = age + gap
    while her_age < 100:
        if (is_age_reversed(age, her_age)):
            age_group.append((age, her_age))
        age += 1
        her_age += 1
    return age_group

def is_age_reversed(age, her_age):
    return str(age).zfill(2) == str(her_age)[::-1].zfill(2)

def solution():
    for gap in range(1, 99):
        groups = age_group_reversed(gap)
        if len(groups) == 8:
            print(groups)
            return groups[5][0]

my_age = solution()
print("Answer: my age is", my_age)

'''
$python3 thinkpython_9_9.py 
[(2, 20), (13, 31), (24, 42), (35, 53), (46, 64), (57, 75), (68, 86), (79, 97)]
Answer: my age is 57
'''

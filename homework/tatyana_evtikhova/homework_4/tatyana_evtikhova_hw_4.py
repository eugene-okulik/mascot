my_dict = {
    'tuple': (1, 5, "Iceland", "Jira", 1996),
    'list': ["Canary Islands", True, 20.07, "defect", None],
    'dict': {"cycle": "cycle 1", "issue": 376, "result1": "Welcome on Home page!", "value": [15, 31, 98], True: 18},
    'set': {66, "issues", "were", "created" "on your behalf"}}

final_element = my_dict['tuple'][-1]
print(final_element)

my_dict['list'].append("test")
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'software'
del my_dict['dict']['cycle']

my_dict['set'].add("Hello worrld")
my_dict['set'].discard(66)

print(my_dict)

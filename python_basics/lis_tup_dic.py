# region List and Tuples
name_lis = ["Tin", "Jona", "Gerard"]
name_tup = ("Tin", "Jona", "Gerard")

# Ordered: Data are assigned with index
print(f"Index 2 of list is {name_lis[2]}")
print(f"Index 1 of tuple is {name_tup[1]}")

# Heterogenous: Can contain any data type inlcuding sequence data types as well
name_lis_hete = ["Tin", "Jona", "Gerard", "1", 2, 0.3, (1, "x", True)]
name_tup_hete = ("Tin", "Jona", "Gerard", "1", 2, 0.3, [1, "x", True])

# Iterable: Can run a for loop through it
for name in name_lis_hete:
    print(type(name))

for name in name_tup_hete:
    print(name)

# Slicing
print(name_lis_hete[1:3])
print(name_tup_hete[:5])

# Membership: Can use 'in' and 'not in'
if 2 in name_lis_hete:
    print("2 is in the list")

if "x" in name_tup_hete:
    print("x is in the tuple")

# Mutability
name_lis.append("RJ")
print(name_lis)
# name_tup.
# endregion

# region Dictionary
# name_dic = {'qa1': 'Tin', 'qa2': 'Jona', 3: 'Gerard'}
name_dic = {
    'qa1': 'Tin',
    'qa2': 'Jona',
    3: 'Gerard',
    4: 'Tester',
    5: 'Tester2'
}
print(name_dic['qa1'])
print(name_dic.get(3))
# endregion


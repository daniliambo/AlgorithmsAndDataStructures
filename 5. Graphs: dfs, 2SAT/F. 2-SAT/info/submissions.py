# frist test
x = """0
01
000
"""
print(x)  # base

x = """1
01
000
"""
print(x)  # base_2 # correct

# second test

x = """1
11
000
"""
print(x)  # wrong

x = """1
00
000
"""
print(x)  # wrong

x = """1
10
000
"""
print(x)  # correct

# third test
x = """1
10
111
"""
print(x)  # correct

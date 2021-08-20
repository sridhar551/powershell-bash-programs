"""
Define "flatten_list" such that the assertions below pass
"""
def flatten_list(input):
    lst = []
    for num in input:
        if type(num) == list or type(num) == tuple:
            lst.extend(flatten_list(num))
        elif type(num) == int:
            lst.append(num)
    return lst


a_list = [1, [2, 3], [4, [5, 6, [10, 11, 12]]], 7, (8, 9)]
assert sorted(flatten_list(a_list)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

b_list = [1, (2, 3, 4), [5, 6, 7], [[[[[8, 9, 10]]]]]]
assert sorted(flatten_list(b_list)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

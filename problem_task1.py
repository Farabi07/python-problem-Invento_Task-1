def get_aspected_index(arr, t_v):
    b = []
    for i in range(0, len(arr)):
        if (arr[i][0] + arr[i][1] == t_v):
            return i

val=[
    [1,5],
    [2,6],
    [1,6],
]

t_b=7

result = get_aspected_index(val, t_b)
print(result)
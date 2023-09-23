result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    for key in data:
        try:
            res = divider(key, data[key])
            result.append(res)
        except(ValueError) as error:
            print(error)
        except(IndexError) as error:
            print(error)
        except:
            print("Error")

    print(result)
except:
    print("ProgramError")

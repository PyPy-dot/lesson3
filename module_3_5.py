def get_multiplied_digits(number:int) -> int:
    num = str(number).replace('0', '')
    def rec(num):
        if len(num) == 1:
            return int(num)
        return int(num[0]) * rec(num[1:])
    return rec(num)

result = get_multiplied_digits(40203)

print(result)
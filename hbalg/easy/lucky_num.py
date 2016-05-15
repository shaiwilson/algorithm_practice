

def lucky_num(n):

    nums = range(1, 11)
    lucky_num = []

    for i in range(n):
        lucky_choice = random.choice(nums)
        nums.remove(lucky_choice)
        lucky_num.append(lucky_choice)

    return lucky_num

print(lucky_num(4))
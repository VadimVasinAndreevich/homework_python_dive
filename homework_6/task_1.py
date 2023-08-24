from random import randint as ri


def position(param):
    print(param)
    if len(set(param)) == len(param):
        return True
    else:
        return False


def position_random():
    count = 1
    max_iter = 4
    while count <= max_iter:
        position_list = [f'{ri(1, 9)}:{ri(1, 9)}' for _ in range(0, 8)]
        if len(set(position_list)) == len(position_list):
            print(position_list)
            count += 1


if __name__ == '__main__':
    print(position([f'{ri(1, 9)}:{ri(1, 9)}' for _ in range(0, 8)]))
    position_random()

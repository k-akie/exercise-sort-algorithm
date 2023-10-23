import copy


def bubble_sort(t: list[int]):
    target = copy.copy(t)

    for i in range(0, len(target) - 1):
        print(target)

        for j in range(len(target) - 1, i, -1):  # 右端から左端まで
            if target[j - 1] > target[j]:  # 右端の一つ左と、右端を比較して、小さければ入れ替える
                tmp = target[j]
                target[j] = target[j - 1]
                target[j - 1] = tmp
        # 最小値が左端になるので、一つ右にずらして同じことを繰り返す

    return target

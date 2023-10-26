import copy


def quick(target: list[int]):
    if len(target) < 2:
        return target

    # 適当に分割する値を決める
    pivot = int((target[0] + target[len(target)-1]) / 2)
    lower = []
    equal = []
    higher = []
    for i in range(0, len(target)):
        if target[i] < pivot:
            lower.append(target[i])
        elif target[i] == pivot:
            # 再帰を止めるために等しい場合を導入したが、本来のクイックソートでは登場しない
            equal.append(target[i])
        else:
            higher.append(target[i])

    lower = quick(lower)
    higher = quick(higher)

    lower.extend(equal)
    lower.extend(higher)
    return lower


def quick_sort(t: list[int]):
    target = copy.copy(t)
    return quick(target)


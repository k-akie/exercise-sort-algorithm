import copy


def sell_sort(t: list[int]):
    target = copy.copy(t)

    h = int(len(target)/2)  # 間隔
    while h > 0:
        for i in range(0, h):
            element_count = int(len(target) / h) - 1
            for j in range(element_count, 0, -1):
                # 右端を挿入する位置を探す
                right = i + j * h
                for k in range(right - h, -1, -h):
                    left = k
                    if target[left] <= target[right]:  # 左と右端を比較して
                        break  # 右端が大きければ終わり
                    else:  # 右端が小さければ入れ替え
                        tmp = target[left]
                        target[left] = target[right]
                        target[right] = tmp

            print(target)

        h = int(h / 2)

    print(target)
    return target

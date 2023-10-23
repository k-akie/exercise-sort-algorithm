import copy


def insertion_sort(t: list[int]):
    target = copy.copy(t)

    for i in range(1, len(target)):
        print(target)

        for j in range(i, 0, -1):  # 左端から、1つずつ増やしながら見ていく
            if target[j - 1] <= target[j]:  # 左隣と今の右端(new)を比較して
                break  # 右端が大きければ終わり
            else:  # 右端が小さければ入れ替え
                tmp = target[j]
                target[j] = target[j - 1]
                target[j - 1] = tmp
        # これで右端(new)が適切な位置に入る

    return target

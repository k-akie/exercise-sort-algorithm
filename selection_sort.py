import copy


def selection_sort(t: list[int]):
    target = copy.copy(t)

    for i in range(0, len(target) - 1):
        print(target)

        # 最小値を見つける
        min_pos = i  # 左端を選択する
        for j in range(i + 1, len(target)):  # 一つ右隣から最後まで
            if target[min_pos] > target[j]:  # 最小値と比較して小さければ
                min_pos = j  # 最小値としてキープする

        # 左端と最小値を入れ替える
        if target[i] > target[min_pos]:  # 左端と最小値を比較して小さければ
            tmp = target[i]
            target[i] = target[min_pos]
            target[min_pos] = tmp

        # これで左端に最小値が来るので、一つ右にずらして同じことを繰り返す

    return target

import copy


def merge_sort(t: list[int]):
    target = copy.copy(t)

    # 最初に要素1個ずつのリストに分割する
    splitLists = [target[idx:idx + 1] for idx in range(0, len(target), 1)]

    while len(splitLists) > 1:
        mergedLists = []

        # 整列済みリスト2組を順にマージする
        for i in range(0, int((len(splitLists) + 1) / 2)):
            # 整列済みリスト2組を選ぶ
            index_a = 2 * i
            index_b = 2 * i + 1
            list_a = splitLists[index_a]
            # 整列済みリストが足りなければ空リストで補完
            list_b = [] if index_b > len(splitLists) - 1 else splitLists[index_b]

            # 整列済みリストのうち、どの位置の要素を扱っているか
            pos_a = 0
            pos_b = 0
            mergedList = []
            while pos_a < len(list_a) or pos_b < len(list_b):
                # 片方のリストが空になっていたら、他方のリストを順に詰める
                if pos_a == len(list_a):
                    mergedList.append(list_b[pos_b])
                    pos_b += 1
                    continue
                if pos_b == len(list_b):
                    mergedList.append(list_a[pos_a])
                    pos_a += 1
                    continue

                # 両リストの先頭のうち、大きい方を詰める
                if list_a[pos_a] > list_b[pos_b]:
                    mergedList.append(list_b[pos_b])
                    pos_b += 1
                else:
                    mergedList.append(list_a[pos_a])
                    pos_a += 1

            # 両リストが空になったら、次に行く
            mergedLists.append(mergedList)
            print(mergedLists)

        splitLists = mergedLists

    return splitLists.pop() if splitLists else []

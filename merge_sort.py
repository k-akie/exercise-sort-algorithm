import copy


def merge_sort(t: list[int]):
    target = copy.copy(t)

    tempList = [target[idx:idx + 1] for idx in range(0, len(target), 1)]
    loop = int(len(target) / 2 + 1)
    while loop > 0:
        # 整列済みリスト2組をマージする
        mergedLists = []
        for i in range(0, int((len(tempList) + 1) / 2)):
            mergedList = []

            if (2 * i + 1) > len(tempList) - 1:
                mergedList = tempList[2 * i]
            else:
                a = tempList[2 * i]
                b = tempList[2 * i + 1]
                pos_a = 0
                pos_b = 0

                while pos_a < len(a) or pos_b < len(b):
                    if pos_a == len(a):
                        mergedList.append(b[pos_b])
                        pos_b += 1
                        continue

                    if pos_b == len(b):
                        mergedList.append(a[pos_a])
                        pos_a += 1
                        continue

                    if a[pos_a] > b[pos_b]:
                        mergedList.append(b[pos_b])
                        pos_b += 1
                        continue

                    mergedList.append(a[pos_a])
                    pos_a += 1

            mergedLists.append(mergedList)
            print(mergedLists)

        tempList = mergedLists
        loop -= 1

    return tempList.pop() if tempList else []

class Item:
    def __init__(self, weight, worth):
        self.weight = weight
        self.worth = worth


def fractionalKnapsack(allItems, sackCapacity):
    allItems.sort(key=lambda x: (x.worth/x.weight), reverse=True)
    sackWorth = 0
    for item in allItems:
        if item.weight <= sackCapacity:
            sackCapacity -= item.weight
            sackWorth += item.worth
        else:
            sackWorth += item.worth * sackCapacity / item.weight
            break
    return sackWorth


if __name__ == '__main__':
    sackCapacity = 100
    allItems = [Item(10, 60), Item(20, 100), Item(30, 120)]
    print(fractionalKnapsack(allItems, sackCapacity))

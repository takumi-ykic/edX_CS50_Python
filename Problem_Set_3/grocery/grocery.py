try:
    items = []
    while True:
        item = input()
        if not item:
            break

        items.append(item.upper())

except EOFError:
    if len(items) != 0:
        counts = {}
        for item in items:
            counts[item] = counts.get(item, 0) + 1

        counts_sorted = sorted(counts.items())

        for item, count in counts_sorted:
            print(f"{count} {item}")


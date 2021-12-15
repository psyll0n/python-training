#! python3


def take(count, iterable):
    conter = 0
    for item in iterable:
        if conter == count:
            return
        conter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, list(distinct(items))):
        print(item)


run_pipeline()

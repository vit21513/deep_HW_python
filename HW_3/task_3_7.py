content = {
    'сапоги': 1.5, 'ружьё': 1.2, 'шампура': 0.5, 'продукты': 7.5, 'термос': 1.5, 'фляжка': 0.3, 'фонарик': 0.5,
    'радиоприемник': 1, 'самогон': 1.0, }

max_weight = 9.0


def backpack_options(goods, max_weight):
    def backtrack(now_items, need_weight):
        if need_weight < 0:
            return []
        if need_weight == 0:
            return [now_items]
        combinations = []
        for item, weight in goods.items():
            if item not in now_items and weight <= need_weight:
                new_items = now_items + [item]
                new_weight = need_weight - weight
                combinations.extend(backtrack(new_items, new_weight))
        return combinations

    return backtrack(list(), max_weight)





max_options = backpack_options(content, max_weight)
print(f"Возможные варианты комплектации рюкзака, грузоподъемность: {max_weight} кг:")
for num, variant in enumerate(max_options, 1):
    print(num, *variant)

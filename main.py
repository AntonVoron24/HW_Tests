def max_stat(stats: dict) -> str:
    return max(stats, key=stats.get)


def unique_values(id_dict: dict) -> list:
    all_id = set(sum(id_dict.values(), []))
    return list(all_id)


def russian_visit(visit_list: list) -> list:
    russian = []
    for visit in visit_list:
        for key, val in visit.items():
            if 'Россия' in val:
                russian.append(visit)
    return russian

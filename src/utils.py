def remove_duplicate_values_from_dict(d):
    trimmed_d = {}
    temp_value = None

    sorted_keys = sorted(d.keys(), key=int)
    last_key = sorted_keys[-1]

    for k in sorted_keys:
        v = d[k]

        if temp_value is None or v != temp_value or k == last_key:
            trimmed_d[k] = v
            temp_value = v

    return trimmed_d

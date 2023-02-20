dct = {
    'person': {
                'in_dict': [1, 2, 3],
                'after_list': {4, '5'},
                'after_set': ('hello', )
              }
       }


def transform_dict(a):
    new_dict = {}
    for key, value in a.items():
        if isinstance(value, dict):
            new_dict.update(transform_dict(value))
        elif isinstance(value, (tuple, list)):
            sub_dict = {}
            for i, sub_value in enumerate(value):
                sub_dict[i] = {key: sub_value}
            new_dict.update({tuple(value): sub_dict})
        else:
            new_dict[key] = value
    return new_dict


print(transform_dict(dct))


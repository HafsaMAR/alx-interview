#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""


import sys


status_code_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
counter = 0

try:
    # Read from stdout
    for line in sys.stdin:
        # split each line using spaces
        line_list = line.split(" ")
        if len(line_list) == 7:
            code = line_list[-2]
            file_size = int(line_list[-1])
            if code in status_code_dict.keys():
                status_code_dict[code] += 1
            total_file_size += file_size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(status_code_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_code_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

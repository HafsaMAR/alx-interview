#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


import sys


total_file_size = 0  # total file size
# dictionary intialized to store the status code frequency
status_code_count = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0  # to count the number of lines at 10 it is re initialized

try:
    # Read stdin line by line
    for line in sys.stdin:
        # automatically splited by spaces
        parts = line.split()
        # now that is splitted lets check the parts
        if (
            len(parts) != 7
            or parts[2] != 'GET'
            or parts[4] not in map(str, status_code_count.keys())
        ):
            continue

        file_size = int(parts[5])
        status_code = int(parts[6])

        # Update metrics
        total_file_size += file_size
        status_code_count[status_code] += 1
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print()


except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{code}: {count}")

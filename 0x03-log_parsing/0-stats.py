#!/usr/bin/python3

import sys
import re

# Define regex pattern to extract relevant information
pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

# Initialize variables
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Match the line format
        match = pattern.match(line)
        if match:
            status_code, file_size = map(int, match.groups())
            # Update total file size
            total_file_size += file_size
            # Update status code count
            status_code_count[status_code] += 1
            line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    # Print final statistics upon keyboard interruption
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

#!/usr/bin/python3
"""Log Parsing"""


import sys
import re


status_counts = {}
total_size = 0
count = 0

pattern = r"^\d+\.\d+\.\d+\.\d+ - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$"  # noqa: E501

try:
    for line in sys.stdin:
        match = re.search(pattern, line)

        if match:
            status = int(match.group(1))
            size = int(match.group(2))

            status_counts[status] = status_counts.get(status, 0) + 1
            total_size += size
            count += 1

            if count % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_counts):
                    print(code, ":", status_counts[code])
except KeyboardInterrupt:
    print("File size:", total_size)
    for code in sorted(status_counts):
        print(code, ":", status_counts[code])

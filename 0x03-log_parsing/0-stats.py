#!/usr/bin/python3
"""Log Parsing"""


import sys


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


def parse_line(line):
    parts = line.split()
    if len(parts) < 7:
        return None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return ip_address, status_code, file_size


def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parsed = parse_line(line)
            if parsed is None:
                continue
            ip_address, status_code, file_size = parsed
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

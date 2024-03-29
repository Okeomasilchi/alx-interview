#!/usr/bin/python3
""" This is a log parsing module """

import sys


def print_stats(total_size, status_codes):
    """
    Print statistics based on the total file
    size and the counts of each
    status code.

    Args:
        total_size (int): The total size of all files processed.
        status_codes (dict): A dictionary containing counts of
        each status code

    Returns:
        None
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


def parse_line(line):
    """
    Parse a log line to extract relevant information.

    Args:
        line (str): A single log line to be parsed.

    Returns:
        tuple or None: A tuple containing the IP address,
        status code, and file size if parsing is successful,
        otherwise None.
    """
    parts = line.split()
    if len(parts) < 9:
        return None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None
    return ip_address, int(status_code), int(file_size)


def main():
    """
    Main function to read log lines from stdin, parse
    them, compute statistics, and print them.

    Returns:
        None
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parsed = parse_line(line)
            if parsed is None:
                continue
            ip_address, status_code, file_size = parsed
            total_size += file_size
            status_codes[status_code] = status_codes.get(
                status_code,
                0
                ) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

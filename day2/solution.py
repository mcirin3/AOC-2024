def is_safe(report):
    """
    Determines if a report is safe based on the criteria:
    - All levels are either increasing or decreasing.
    - Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are either positive or negative (increasing or decreasing)
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return all_increasing or all_decreasing


def can_be_made_safe(report):
    """
    Checks if removing a single level from the report makes it safe.
    """
    for i in range(len(report)):
        # Create a new report without the i-th level
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports(file_path, use_dampener=False):
    """
    Reads the input file and counts the number of safe reports.
    If use_dampener is True, considers the Problem Dampener logic.
    """
    safe_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report) or (use_dampener and can_be_made_safe(report)):
                safe_count += 1

    return safe_count


# Main Execution
if __name__ == "__main__":
    file_path = "input.txt"  # Input file name

    # Part 1: Without the Problem Dampener
    safe_reports_part1 = count_safe_reports(file_path, use_dampener=False)
    print(f"Part 1 - Number of safe reports: {safe_reports_part1}")

    # Part 2: With the Problem Dampener
    safe_reports_part2 = count_safe_reports(file_path, use_dampener=True)
    print(f"Part 2 - Number of safe reports (with Dampener): {safe_reports_part2}")
import argparse
import os
from datetime import datetime
import re
import colorama
from colorama import Fore, Style

colorama.init()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The name of the file or directory to analyze.")
    parser.add_argument("-d", "--date", help="Specify a date range (YYYY-MM-DD HH:MM:SS.milliseconds - YYYY-MM-DD "
                                             "HH:MM:SS.milliseconds) or a single date for filtering the logs.",
                        default=None)
    parser.add_argument("-t", "--text", help="Specify a text string to search for within the logs.", default=None)
    parser.add_argument("-u", "--unwanted", help="Specify a text string or a list of strings (comma-separated) to "
                                                 "filter out logs.", default=None)
    args = parser.parse_args()
    return args


def is_file_or_directory(path):
    if os.path.isfile(path):
        return "file"
    elif os.path.isdir(path):
        return "directory"
    else:
        return None


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def read_files(directory_path):
    files_content = {}
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} not found.")
        return files_content

    if not os.path.isdir(directory_path):
        print(f"{directory_path} is not a directory.")
        return files_content

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            content = read_file(file_path)
            if content:
                files_content[file_name] = content
    return files_content


def filter_logs(logs, start_date=None, end_date=None, text=None, unwanted=None):
    total_logs = len(logs)
    filtered_logs_count = 0
    filtered_logs = {}

    for log_time_str, log_message in logs.items():
        match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', log_message)
        if match:
            log_time_str = match.group()
            log_time = datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S.%f")

            if start_date and end_date:
                if not (start_date <= log_time <= end_date):
                    continue

            if unwanted:
                if any(unwanted_text.lower() in log_message.lower() for unwanted_text in unwanted):
                    continue

            if text:
                text_match = re.search(re.escape(text), log_message, re.IGNORECASE)
                if text_match:
                    start_index = max(0, text_match.start() - 150)
                    end_index = min(len(log_message), text_match.end() + 150)
                    log_message = log_message[start_index:end_index]
                else:
                    continue

            filtered_logs[log_time_str] = log_message
            filtered_logs_count += 1

    return filtered_logs, total_logs, filtered_logs_count


def print_logs(logs):
    for log_time_str, log_message in logs.items():
        log_time_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', log_message)
        if log_time_match:
            log_time_str_with_milliseconds = log_time_match.group()
            print(Fore.YELLOW + log_time_str_with_milliseconds + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + log_time_str + Style.RESET_ALL)

        if len(log_message) > 300:
            print(log_message[:300])
        else:
            print(log_message)


def main():
    args = parse_arguments()
    file_type = is_file_or_directory(args.file)

    if file_type == "file":
        logs = {args.file: read_file(args.file)}
    elif file_type == "directory":
        logs = read_files(args.file)
    else:
        print(f"{args.file} does not exist or is not a valid file or directory.")
        return

    start_date = None
    end_date = None

    if args.date and ' - ' in args.date:
        try:
            start_date_str, end_date_str = args.date.split(' - ')
            start_date = datetime.strptime(start_date_str.strip(), "%Y-%m-%d %H:%M:%S.%f")
            end_date = datetime.strptime(end_date_str.strip(), "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            print("Error: Invalid date range format. Please use YYYY-MM-DD HH:MM:SS.milliseconds - YYYY-MM-DD "
                  "HH:MM:SS.milliseconds")
            return
    elif args.date:
        try:
            start_date = datetime.strptime(args.date, "%Y-%m-%d %H:%M:%S.%f")
            end_date = start_date
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD HH:MM:SS.milliseconds")
            return

    filtered_logs, total_logs, filtered_logs_count = filter_logs(logs, start_date, end_date, args.text, args.unwanted)

    print_logs(filtered_logs)
    print(f"Total logs: {total_logs}")
    print(f"Filtered logs: {filtered_logs_count}")


if __name__ == "__main__":
    main()

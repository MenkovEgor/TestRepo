import json
import datetime

PRODUCT_VERSION_PATTERN = "Product version:"
JSON_CONFIG_FILE_PATH = "json_config_file.txt"

def parse_log_file(in_file_path, expected_version, out_file_path, log_level: object, start_time, end_time):
    with open(in_file_path, "r") as file:
        version_line = file.readline()
        cur_version = get_version(version_line)

        if cur_version != expected_version:
            raise Exception("Invalid version: {number}".format(number=cur_version))

        result_records = []

        for line in file:
            # Joining date and time into one string
            interval_time = line.split(' ')[0] + ' ' + line.split(' ')[1]
            if line.split(' ')[2] in log_level:
                if date_matching(start=start_time, end=end_time, match=interval_time):
                    result_records.append(line)

        if result_records:
            with open(out_file_path, "w") as out_file:
                out_file.writelines(result_records)

            print("Result records saved.")


def get_version(version_str: object) -> object:
    if version_str.startswith(PRODUCT_VERSION_PATTERN):
        version_number = version_str[len(PRODUCT_VERSION_PATTERN):]
        return version_number.strip()
    else:
        raise Exception("Invalid file format, version is missing")

def date_matching(start, end, match):
    #Converting strings into datetime format for further matching
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
    match_date = datetime.datetime.strptime(match, '%Y-%m-%d %H:%M:%S.%f')
    if start_date <= match_date <= end_date:
        return True
    else:
        return False

if __name__ == "__main__":
    # Read from JSON file
    with open(JSON_CONFIG_FILE_PATH, "r") as file:
        config_json_string = file.read()
        parsed_config_json = json.loads(config_json_string)
    # Main function
    try:
        parse_log_file(in_file_path=parsed_config_json['in_file_path'],
                       expected_version=parsed_config_json['version'],
                       out_file_path=parsed_config_json['out_file_path'],
                       log_level=parsed_config_json['Error_levels'],
                       start_time="2017-07-24 07:32:33.132",
                       end_time="2017-07-24 07:33:00.132")
    except IOError as e:
        print(str(e))
    except Exception as e:
        print(str(e))

import re as regex
from datetime import datetime

from DataPreparator.Constants import FormatConstants
from DataPreparator.Constants import RegexConstants


class AccessLogReader:

    def __init__(self):
        self.access_log_list = []

    def read_file(self, file_path: str) -> list:
        with open(file_path) as file:
            reader = file.readlines()

            for row in reader:
                value_set = AccessLogReader.extract_values_from_row(row)
                self.access_log_list.append(value_set)

        return self.access_log_list

    @staticmethod
    def extract_values_from_row(row: str) -> list:
        extracted_values = []

        ip_address = AccessLogReader.regex_value_extractor(row, RegexConstants.IP_ADDRESS_REGEX)
        extracted_values.append(ip_address)

        timestamp_string = AccessLogReader.regex_value_extractor(row, RegexConstants.TIMESTAMP_REGEX)
        timestamp = AccessLogReader.string_to_datetime_converter(timestamp_string)
        extracted_values.append(timestamp)

        http_method = AccessLogReader.regex_value_extractor(row, RegexConstants.HTTP_METHOD_REGEX)
        extracted_values.append(http_method)

        url = AccessLogReader.regex_value_extractor(row, RegexConstants.URL_REGEX)
        extracted_values.append(url)

        status_code = AccessLogReader.regex_value_extractor(row, RegexConstants.RESPONSE_CODE_REGEX)
        extracted_values.append(status_code)

        http_version = AccessLogReader.regex_value_extractor(row, RegexConstants.HTTP_VERSION_REGEX)
        extracted_values.append(http_version)

        endpoint = AccessLogReader.get_endpoint_from_access_log(row)
        extracted_values.append(endpoint)

        user_agent = AccessLogReader.get_user_agent_string_from_access_log(row)
        extracted_values.append(user_agent)

        return extracted_values

    @staticmethod
    def string_to_datetime_converter(date_string: str) -> datetime:
        datetime_object = datetime.strptime(date_string, FormatConstants.DATETIME_FORMAT)

        return datetime_object

    @staticmethod
    def regex_value_extractor(access_log: str, regex_string: str) -> str:
        regex_term = regex.compile(regex_string)
        result = regex_term.search(access_log)

        if result is not None:
            return result.group()

        return 'None'

    @staticmethod
    def regex_substring_remover(access_log: str, regex_string: str) -> str:
        regex_term = regex.compile(regex_string)
        substring_to_delete = regex_term.search(access_log)

        reduced_string = access_log.replace(substring_to_delete.group(), '')

        return reduced_string

    @staticmethod
    def get_endpoint_from_access_log(access_log: str) -> str:
        result = access_log.split('"')[1::2]
        substring_with_endpoint = result[0]

        endpoint_without_http_method = AccessLogReader.regex_substring_remover(
            substring_with_endpoint,
            RegexConstants.HTTP_METHOD_REGEX
        )

        endpoint = AccessLogReader.regex_substring_remover(endpoint_without_http_method, RegexConstants.HTTP_VERSION_REGEX)

        endpoint_without_whitespace = endpoint.replace(' ', '')

        return endpoint_without_whitespace

    @staticmethod
    def get_user_agent_string_from_access_log(access_log: str) -> str:
        result = access_log.split('"')[1::2]
        user_agent_string = result[2]

        return user_agent_string

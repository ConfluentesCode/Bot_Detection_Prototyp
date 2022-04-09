import re as regex
from datetime import datetime

from DataPreparator.Constants import FormatConstants
from DataPreparator.Constants import RegexConstants


class AccessLogReader:

    def __init__(self):
        self.access_log_list = []
        self.row_counter = 0

    def read_file(self, file_path: str) -> list:
        with open(file_path) as file:
            reader = file.readlines()

            for row in reader:
                value_set = AccessLogReader.extract_values_from_row(row)
                self.access_log_list.append(value_set)
                self.row_counter += 1
                print('read row:', self.row_counter)

        return self.access_log_list

    @staticmethod
    def extract_values_from_row(row: str) -> list:
        extracted_values = []

        ip_address = AccessLogReader.get_ip_address_from_access_log(row)
        extracted_values.append(ip_address)

        timestamp = AccessLogReader.get_timestamp_from_access_log(row)
        extracted_values.append(timestamp)

        http_method = AccessLogReader.get_http_methode_from_access_log(row)
        extracted_values.append(http_method)

        resource = AccessLogReader.get_resource_from_access_log(row)
        extracted_values.append(resource)

        http_version = AccessLogReader.get_http_version_from_access_log(row)
        extracted_values.append(http_version)

        status_code = AccessLogReader.get_status_code_from_access_log(row)
        extracted_values.append(status_code)

        referer = AccessLogReader.get_referer_from_access_log(row)
        extracted_values.append(referer)

        user_agent = AccessLogReader.get_user_agent_string_from_access_log(row)
        extracted_values.append(user_agent)

        return extracted_values

    @staticmethod
    def get_ip_address_from_access_log(access_log: str) -> str:
        ip_address = AccessLogReader.regex_value_extractor(access_log, RegexConstants.IP_ADDRESS_REGEX)

        if ip_address is None:
            return 'None'

        return ip_address

    @staticmethod
    def get_timestamp_from_access_log(access_log: str):
        timestamp_string = AccessLogReader.regex_value_extractor(access_log, RegexConstants.TIMESTAMP_REGEX)

        if timestamp_string is None:
            return AccessLogReader.string_to_datetime_converter('01/Jan/0001:00:00:00 +0100')

        return AccessLogReader.string_to_datetime_converter(timestamp_string)

    @staticmethod
    def get_http_methode_from_access_log(access_log: str) -> str:
        http_methode = AccessLogReader.regex_value_extractor(access_log, RegexConstants.HTTP_METHOD_REGEX)

        if http_methode is None:
            return 'None'

        return http_methode

    @staticmethod
    def get_resource_from_access_log(access_log: str) -> str:
        result = access_log.split('"')[1::2]
        resource_substring = result[0]

        resource_substring_split = resource_substring.split(' ')

        list_length = len(resource_substring_split)

        if list_length > 1:
            resource = resource_substring_split[1]
            return resource

        if list_length != 3:
            return 'None'

        return 'None'

    @staticmethod
    def get_http_version_from_access_log(access_log: str) -> str:
        http_version = AccessLogReader.regex_value_extractor(access_log, RegexConstants.HTTP_VERSION_REGEX)

        if http_version is None:
            return 'None'

        return http_version

    @staticmethod
    def get_status_code_from_access_log(access_log: str) -> int:
        status_code_string = AccessLogReader.regex_value_extractor(access_log, RegexConstants.RESPONSE_CODE_REGEX)

        if status_code_string is None:
            return 999

        status_code = int(status_code_string)

        return status_code

    @staticmethod
    def get_referer_from_access_log(access_log: str) -> str:
        referer = AccessLogReader.regex_value_extractor(access_log, RegexConstants.URL_REGEX)

        if referer is None:
            return 'None'

        return referer

    @staticmethod
    def get_user_agent_string_from_access_log(access_log: str) -> str:
        result = access_log.split('"')[1::2]
        user_agent_string = result[2]

        return user_agent_string

    @staticmethod
    def string_to_datetime_converter(date_string: str) -> datetime:
        datetime_object = datetime.strptime(date_string, FormatConstants.DATETIME_FORMAT)

        return datetime_object

    @staticmethod
    def regex_value_extractor(access_log: str, regex_string: str):
        regex_term = regex.compile(regex_string)
        result = regex_term.search(access_log)

        if result is not None:
            return result.group()

        return None

    @staticmethod
    def regex_substring_remover(access_log: str, regex_string: str) -> str:
        regex_term = regex.compile(regex_string)
        substring_to_delete = regex_term.search(access_log)

        reduced_string = access_log.replace(substring_to_delete.group(), '')

        return reduced_string

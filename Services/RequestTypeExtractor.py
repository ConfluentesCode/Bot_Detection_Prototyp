import re as regex
from Constants import Constants
from Enum.RequestType import RequestType


class RequestTypeExtractor:

    def get_request_type_from_uri(self, uri: str):
        if self.is_uri_part_of_group(Constants.TEXT_GROUP_REGEX, uri):
            return RequestType.TEXT
        elif self.is_uri_part_of_group(Constants.WEB_GROUP_REGEX, uri):
            return RequestType.WEB
        elif self.is_uri_part_of_group(Constants.DOC_GROUP_REGEX, uri):
            return RequestType.DOC
        elif self.is_uri_part_of_group(Constants.AV_GROUP_REGEX, uri):
            return RequestType.AV
        elif self.is_uri_part_of_group(Constants.PROG_GROUP_REGEX, uri):
            return RequestType.PROG
        elif self.is_uri_part_of_group(Constants.COMPRESSED_GROUP_REGEX, uri):
            return RequestType.COMPRESSED
        else:
            return RequestType.NOE

    @staticmethod
    def is_uri_part_of_group(regex_string: str, uri: str):

        regex_term = regex.compile(regex_string)
        result = regex_term.search(uri)

        if result is not None:
            return True

        return False

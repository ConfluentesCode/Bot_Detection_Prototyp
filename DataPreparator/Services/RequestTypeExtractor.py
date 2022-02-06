import re as regex
from DataPreparator.Constants import RegexConstants
from DataPreparator.Enums.RequestType import RequestType


class RequestTypeExtractor:

    def get_request_type_from_resource(self, resource: str):
        if self.is_resource_part_of_group(RegexConstants.TEXT_GROUP_REGEX, resource):
            return RequestType.TEXT
        elif self.is_resource_part_of_group(RegexConstants.WEB_GROUP_REGEX, resource):
            return RequestType.WEB
        elif self.is_resource_part_of_group(RegexConstants.DOC_GROUP_REGEX, resource):
            return RequestType.DOC
        elif self.is_resource_part_of_group(RegexConstants.AV_GROUP_REGEX, resource):
            return RequestType.AV
        elif self.is_resource_part_of_group(RegexConstants.PROG_GROUP_REGEX, resource):
            return RequestType.PROG
        elif self.is_resource_part_of_group(RegexConstants.COMPRESSED_GROUP_REGEX, resource):
            return RequestType.COMPRESSED
        else:
            return RequestType.NOE

    @staticmethod
    def is_resource_part_of_group(regex_string: str, resource: str):

        regex_term = regex.compile(regex_string)
        result = regex_term.search(resource)

        if result is not None:
            return True

        return False

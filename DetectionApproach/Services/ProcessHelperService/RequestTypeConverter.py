class RequestTypeConverter:

    @staticmethod
    def convert_request_pattern(resource_pattern):
        converted_resource_pattern = []

        for resource in resource_pattern:
            converted_resource = resource.value
            converted_resource_pattern.append(converted_resource)

        return converted_resource_pattern

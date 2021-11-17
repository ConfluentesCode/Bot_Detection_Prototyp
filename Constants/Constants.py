ACCESS_LOG_FILE_PATH = '/Users/bjarneschroeder/PycharmProjects/Bot_Detection_Prototyp/InputFiles/logfiles.csv'
DATABASE_PATH = 'sqlite:////Users/bjarneschroeder/PycharmProjects/Bot_Detection_Prototyp/DatabaseConnector/Database/BotDetection.db'

IP_ADDRESS_REGEX = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
TIMESTAMP_REGEX = r"\d{2}/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}"
HTTP_METHOD_REGEX = r"(POST|DELETE|GET|PUT)"
URL_REGEX = r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
RESPONSE_CODE_REGEX = r"303|404|500|403|502|304|200"
HTTP_VERSION_REGEX = r"HTTP/\d{1}\.\d{1}"

DATETIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"

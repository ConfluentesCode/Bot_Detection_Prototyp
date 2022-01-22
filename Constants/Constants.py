ACCESS_LOG_FILE_PATH = '/Users/bjarneschroeder/PycharmProjects/Bot_Detection_Prototyp/InputFiles/logfiles_iran_short.log'
UDGER_PATH = '/Users/bjarneschroeder/PycharmProjects/Bot_Detection_Prototyp/DatabaseConnector/Database/'

IP_ADDRESS_REGEX = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
TIMESTAMP_REGEX = r"\d{2}/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}"
HTTP_METHOD_REGEX = r"(POST|DELETE|GET|PUT|HEAD)"
URL_REGEX = r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
RESPONSE_CODE_REGEX = r"303|404|500|403|502|304|200"
HTTP_VERSION_REGEX = r"HTTP/\d{1}\.\d{1}"

TEXT_GROUP_REGEX = r"(.txt|.xml|.sty|.tex|.cpp|.java)"
WEB_GROUP_REGEX = r"(.html|.htm|.asp|.jsp|.php|.cgi|.js)"
DOC_GROUP_REGEX = r"(.xls|.doc|.ppt|.pdf|.ps|.dvi)"
AV_GROUP_REGEX = r"(.avi|.mp3|.wmv|.mpg)"
PROG_GROUP_REGEX = r"(.exe|.dll|.dat|.msi|.jar)"
COMPRESSED_GROUP_REGEX = r"(.zip|.rar|.gzip|.tar|.gz|.7z)"

DATETIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"

FILL_DATABASE_TOGGLE = False
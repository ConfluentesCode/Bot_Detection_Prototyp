from datetime import datetime

from DatabaseConnector.DatabaseSettings import SessionCreator
from DatabaseConnector.Models.AccessLog import AccessLog
from DatabaseConnector.Models.Request import Request
from DatabaseConnector.Models.Session import Session
from DatabaseConnector.Models.Result import Result
from DatabaseConnector.Models.ScoringParameters import ScoringParameters


class DataSaver:
    session_creator = SessionCreator()

    def save_access_log_list(self, access_log_entry_list: list):
        for access_log_entry in access_log_entry_list:
            access_log_model = AccessLog(ip_address=access_log_entry[0], timestamp=access_log_entry[1],
                                         http_method=access_log_entry[2], resource=access_log_entry[3],
                                         http_version=access_log_entry[4], status_code=access_log_entry[5],
                                         referer=access_log_entry[6], user_agent=access_log_entry[7])
            self.session_creator.add(access_log_model)

        self.session_creator.commit()

    # Annahme ist, dass der user-agent waehrend der sesssion identisch bleibt und die ip-addresse nur einmal auftaucht
    def save_user_session(self, ip_address, user_agent, is_bot):
        session_model = Session(session_ip_address=ip_address,
                                session_useragent=user_agent, is_Bot=is_bot, )
        self.session_creator.add(session_model)
        self.session_creator.commit()

    def save_request_from_session(self, session_access_log, request_type, session_id):
        request_model = Request(timestamp=session_access_log.timestamp, http_method=session_access_log.http_method,
                                resource=session_access_log.resource, status_code=session_access_log.status_code,
                                referer=session_access_log.referer, request_type=request_type,
                                session_id=session_id)
        self.session_creator.add(request_model)
        self.session_creator.commit()

    def save_test_result(self, group_id, test_result):
        session_id = test_result[0]
        human_prob = test_result[1]
        bot_prob = test_result[2]
        chain_decision = test_result[3]

        result_model = Result(session_id=session_id, group_id=group_id, human_prob=human_prob, bot_prob=bot_prob,
                              is_bot_decision=chain_decision)

        self.session_creator.add(result_model)
        self.session_creator.commit()

    def save_performance_parameter(self, detection_approach, precision, recall, accuracy, f1):
        parameter_model = ScoringParameters(test_date=datetime.now(), detection_approach=detection_approach,
                                            recall=recall, precision=precision, f1=f1, accuracy=accuracy)

        self.session_creator.add(parameter_model)
        self.session_creator.commit()

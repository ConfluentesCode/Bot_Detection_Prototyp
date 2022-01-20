from udger import Udger
from Constants import Constants


class BotSessionIdentifier:
    udger = Udger(Constants.UDGER_PATH)

    def is_user_session_from_bot(self, session_user_agent, session_ip_address):
        ua_check_result = self.verify_user_agent(session_user_agent)

        if ua_check_result is True:
            return True

        ip_check_result = self.verify_ip_address(session_ip_address)

        if ip_check_result is True:
            return True

        return False

    def verify_user_agent(self, user_agent):
        ua_result = self.udger.parse_ua(user_agent)
        ua_class_code = ua_result['ua_class_code']

        if ua_class_code == 'crawler' or ua_class_code == 'validator' or ua_class_code == 'email_client' or ua_class_code == 'multimedia_player' or ua_class_code == 'offline_browser':
            return True

        return False

    def verify_ip_address(self, ip_address):
        ip_result = self.udger.parse_ip(ip_address)
        ip_classification_code = ip_result['ip_classification_code']

        if ip_classification_code == 'crawler' or ip_classification_code == 'fake_crawler' or ip_classification_code == 'known_attack_source' or ip_classification_code == 'known_attack_source_ssh' or ip_classification_code == 'known_attack_source_mail':
            return True

        return False


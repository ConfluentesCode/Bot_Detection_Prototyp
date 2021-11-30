from DatabaseConnector.DatabaseSettings import SessionCreator
from Models.AccessLog import AccessLog
from Models.Session import Session


class DataLoader:
    session_creator = SessionCreator()

    def get_users_from_access_log(self):
        query_results = self.session_creator.query(AccessLog.ip_address).group_by(AccessLog.ip_address).all()

        user_ip_address_list = [value for value, in query_results]

        return user_ip_address_list

    def get_user_session_from_ip(self, user_ip: str):
        user_session = self.session_creator.query(AccessLog).filter(AccessLog.ip_address == user_ip).all()

        return user_session

    def get_session_id_from_ip_address(self, ip_address):
        session = self.session_creator.query(Session).filter(Session.session_ip_address == ip_address).first()

        return session.session_id




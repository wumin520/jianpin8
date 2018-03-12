# -*- coding: utf-8 -*-
from jianpin import db


class GlobalFunctions:
    @staticmethod
    def db_commit_or_rollback():
        """
        提交所有 session
        :return:
        """
        for session in db._sessions.values():
            try:
                session.commit()
            except:
                session.rollback()
                raise

    @staticmethod
    def db_rollback():
        """
        rollback 所有 session
        :return:
        """
        for session in db._sessions.values():
            session.rollback()
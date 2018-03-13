# -*- coding: utf-8 -*-
from jianpin import db
from jianpin.bll import BaseBll


class CityBll(BaseBll):

    def fetch_all(self):
        """

        :return:
        """

        return db.session.execute(
            """
            SELECT * FROM cities
            """,
        ).fetchall()

    def fetch_by_ids(self, ids):
        """

        :return:
        """

        return db.session.execute(
            """
            SELECT * FROM cities WHERE id in :ids
            """,
            {
                'ids': ids
            }
        ).fetchall()

    def get_by_id(self, city_id):
        """

        :param city_id:
        :return:
        """
        return db.session.execute(
            """
            SELECT * FROM cities WHERE id = :id
            """,
            {
                'id': city_id
            }
        ).fetchone()

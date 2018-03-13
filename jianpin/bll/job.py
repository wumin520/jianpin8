# -*- coding: utf-8 -*-
import logging

import math

from jianpin import db
from jianpin.bll import BaseBll

logger = logging.getLogger(__name__)


class JobBll(BaseBll):

    def fetch_list_data(self, city_id, page=1, pagesize=50):
        """

        :param city_id:
        :param page:
        :param pagesize:
        :return:
        """

        total = self.get_count(city_id)
        logger.debug('fetch_list_data total:%s' % total)
        if total == 0:
            return []

        total_page = math.ceil(total / pagesize)
        page = page or 1
        if page > total_page:
            return []

        offset = (page - 1) * pagesize
        where = ''
        if city_id:
            where = 'WHERE city_id = :city_id'
        rows = db.session.execute(
            """
            SELECT * FROM jobs {} ORDER BY sort ASC, id DESC
            LIMIT {},{}
            """.format(where, offset, pagesize),
            {
                'city_id': city_id
            }
        ).fetchall()
        return rows

    def fetch_search_data(self, city_id, keywords, page=1, pagesize=50):
        """

        :param city_id:
        :param keywords:
        :param page:
        :param pagesize:
        :return:
        """

        total = self.get_search_count(city_id, keywords)
        logger.debug('fetch_search_data total:%s' % total)
        if total == 0:
            return []

        total_page = math.ceil(total / pagesize)
        page = page or 1
        if page > total_page:
            return []

        offset = (page - 1) * pagesize
        where = 'WHERE title like \'%{}%\''.format(keywords)
        if city_id:
            where += ' AND city_id = :city_id'
        rows = db.session.execute(
            """
            SELECT * FROM jobs {} ORDER BY sort ASC, id DESC
            LIMIT {},{}
            """.format(where, offset, pagesize),
            {
                'city_id': city_id
            }
        ).fetchall()
        return rows

    def get_count(self, city_id):
        """

        :param city_id:
        :return:
        """
        where = ''
        if city_id:
            where = 'WHERE city_id = :city_id'

        row = db.session.execute(
            """
            SELECT count(id) as cnt FROM jobs {}
            """.format(where),
            {
                'city_id': city_id
            }
        ).fetchone()
        if row and row.cnt:
            return row.cnt
        return 0

    def get_search_count(self, city_id, keywords):
        """

        :param city_id:
        :param keywords:
        :return:
        """
        where = 'WHERE title like \'%{}%\''.format(keywords)
        if city_id:
            where += ' AND city_id = :city_id'

        row = db.session.execute(
            """
            SELECT count(id) as cnt FROM jobs {}
            """.format(where),
            {
                'city_id': city_id
            }
        ).fetchone()
        if row and row.cnt:
            return row.cnt
        return 0

    def get_by_id(self, id):
        """

        :param id:
        :return:
        """
        return db.session.execute(
            """
            SELECT * FROM jobs WHERE id = :id
            """,
            {
                'id': id
            }
        ).fetchone()

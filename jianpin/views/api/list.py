# -*- coding: utf-8 -*-
from flask import request

from jianpin import app
from jianpin.bll.city import CityBll
from jianpin.bll.job import JobBll
from jianpin.views.api import success, get_or_exception
from jianpin.consts import JIANPIN_CURRENCY_UNIT, JIANPIN_JIEXI_TYPE

@app.route('/api/job.list')
def job_list():
    """
    doc/list.md
    :return:
    """

    city_id = get_or_exception('city_id', request.args, ptype='int', default=0)
    offset = get_or_exception('offset', request.args, ptype='int', default=0)
    pagesize = get_or_exception('pagesize', request.args, ptype='int',
                                default=50)

    rows = JobBll.get_instance().fetch_list_data(
        city_id=city_id, page=offset, pagesize=pagesize)

    city_ids = [row.city_id for row in rows]
    cities = CityBll.get_instance().fetch_by_ids(list(set(city_ids)))

    payload = []
    for row in rows:
        jianpin_startdate = ''
        if row.jianpin_startdate:
            startdate = row.jianpin_startdate.strftime('%Y-%m-%d')
            jianpin_startdate = startdate[5:7] + '.' + startdate[8:10]

        jianpin_enddate = ''
        if row.jianpin_enddate:
            enddate = row.jianpin_enddate.strftime('%Y-%m-%d')
            jianpin_enddate = enddate[5:7] + '.' + enddate[8:10]

        jianpin_type = "长期招聘"
        if row.jianpin_type == 2:
            if jianpin_startdate and jianpin_enddate:
                jianpin_type = jianpin_startdate + '-' + jianpin_enddate

        # 日期截取
        payload.append({
            'id': row.id,
            'title': row.title,
            'city_name': cities[row.city_id].city_name,
            'hot_tag': row.hot_tag,
            'jianpin_type': jianpin_type,
            'currency': row.currency,
            'currency_unit': JIANPIN_CURRENCY_UNIT[row.currency_unit],
            'jiexi_type': JIANPIN_JIEXI_TYPE[row.jiexi_type],
        })

    return success(payload)

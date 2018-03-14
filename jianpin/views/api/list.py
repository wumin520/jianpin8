# -*- coding: utf-8 -*-
from flask import request

from jianpin import app
from jianpin.bll.city import CityBll
from jianpin.bll.job import JobBll
from jianpin.views.api import success, get_or_exception


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

    payload = []

    city_ids = dict()
    for row in rows:
        city_ids[row.id] = row.id

    cities = CityBll.get_instance().fetch_by_ids(list(city_ids.keys()))

    for row in rows:
        jianpin_starttime = ''
        if row.jianpin_starttime:
            jianpin_starttime = row.jianpin_starttime.strftime('%Y-%m-%d '
                                                               '%H:%M:%S')
        jianpin_endtime = ''
        if row.jianpin_endtime:
            jianpin_endtime = row.jianpin_endtime.strftime('%Y-%m-%d %H:%M:%S')

        payload.append({
            'id': row.id,
            'title': row.title,
            'city_name': cities[row.id].city_name,
            'tag': row.hot_tag,
            'jianpin_starttime': jianpin_starttime,
            'jianpin_endtime': jianpin_endtime,
            'currency': row.currency,
            'currency_unit': row.currency_unit,
            'jiexi_type': row.jiexi_type,
        })

    return success(payload)

# -*- coding: utf-8 -*-
from flask import request

from jianpin import app
from jianpin.bll.city import CityBll
from jianpin.bll.job import JobBll
from jianpin.views.api import success, get_or_exception


@app.route('/api/job.search')
def job_list():
    """
    doc/search.md
    :return:
    """

    city_id = get_or_exception('city_id', request.args, ptype='int', default=0)
    offset = get_or_exception('offset', request.args, ptype='int', default=0)
    pagesize = get_or_exception('pagesize', request.args, ptype='int',
                                default=50)
    keywords = get_or_exception('keywords', request.args, ptype='str')

    keywords = '%{}%'.format(keywords)

    rows = JobBll.get_instance().fetch_search_data(city_id=city_id,
                                                   keywords=keywords,
                                                   page=offset,
                                                   pagesize=pagesize)

    payload = []

    city_ids = dict()
    for row in rows:
        city_ids[row.id] = row.id

    cities = CityBll.get_instance().fetch_by_ids(list(city_ids.keys()))

    for row in rows:
        jianpin_startdate = ''
        if row.jianpin_startdate:
            startdate = row.jianpin_startdate
            jianpin_startdate = startdate[5:7] + '.' + startdate[8:10]

        jianpin_enddate = ''
        if row.jianpin_enddate:
            enddate = row.jianpin_enddate
            jianpin_enddate = enddate[5:7] + '.' + enddate[8:10]

        jianpin_type = "长期招聘"
        if row.jianpin_type == 2:
            if jianpin_startdate and jianpin_enddate:
                jianpin_type = jianpin_startdate + '-' + jianpin_enddate

        payload.append({
            'id': row.id,
            'title': row.title,
            'city_name': cities[row.id].city_name,
            'hot_tag': row.hot_tag,
            'jianpin_type': jianpin_type,
            'currency': row.currency,
            'currency_unit': row.currency_unit,
            'jiexi_type': row.jiexi_type,
        })

    return success(payload)

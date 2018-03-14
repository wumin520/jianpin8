# -*- coding: utf-8 -*-
from flask import request

from jianpin import app
from jianpin.bll.city import CityBll
from jianpin.bll.job import JobBll
from jianpin.views.api import success, APIException, get_or_exception


@app.route('/api/job.detail')
def city_list():
    """

    :return:
    """

    id = get_or_exception('id', request.args, ptype='int')

    job = JobBll.get_instance().get_by_id(id)
    if not job:
        raise APIException(err_msg='内容不存在')

    city = CityBll.get_instance().get_by_id(job.city_id)
    jianpin_starttime = ''
    if job.jianpin_starttime:
        jianpin_starttime = job.jianpin_starttime.strftime('%Y-%m-%d %H:%M:%S')
    jianpin_endtime = ''
    if job.jianpin_endtime:
        jianpin_endtime = job.jianpin_endtime.strftime('%Y-%m-%d %H:%M:%S')
    work_time = ''
    if job.work_time:
        work_time = job.work_time.strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        'id': job.id,
        'title': job.title,
        'city_name': city.city_name,
        'tag': job.hot_tag,
        'jianpin_type': job.jianpin_type,
        'jianpin_starttime': jianpin_starttime,
        'jianpin_endtime': jianpin_endtime,
        'currency': job.currency,
        'currency_unit': job.currency_unit,
        'jiexi_type': job.jiexi_type,
        'jianpin_person': job.jianpin_person,
        'jianpin_detail': job.jianpin_detail,
        'welfare': job.welfare,
        'work_time': work_time,
        'work_adress': job.work_adress,
        'company': job.company,
        'jump_url': job.jump_url,
        'jump_type': job.jump_type,
    }

    return success(payload)

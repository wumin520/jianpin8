# -*- coding: utf-8 -*-
from flask import request

from jianpin import app
from jianpin.bll.city import CityBll
from jianpin.bll.job import JobBll
from jianpin.views.api import success, APIException, get_or_exception
from jianpin.consts import JIANPIN_CURRENCY_UNIT, JIANPIN_JIEXI_TYPE

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

    payload = {
        'id': job.id,
        'title': job.title,
        'city_name': city.city_name,
        'hot_tag': job.hot_tag,
        'currency': job.currency,
        'currency_unit': JIANPIN_CURRENCY_UNIT[job.currency_unit],
        'jiexi_type': JIANPIN_JIEXI_TYPE[job.jiexi_type],
        'jianpin_person': job.jianpin_person,
        'jianpin_detail': job.jianpin_detail,
        'welfare': job.welfare,
        'work_time': job.work_time,
        'work_adress': job.work_adress,
        'company': job.company,
        'jump_url': job.jump_url,
        'jump_type': job.jump_type,
    }

    return success(payload)

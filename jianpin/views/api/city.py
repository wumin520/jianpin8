# -*- coding: utf-8 -*-
from jianpin import app
from jianpin.bll.city import CityBll
from jianpin.views.api import success


@app.route('/api/city.list')
def city_list():
    """

    :return:
    """

    cities = CityBll.get_instance().fetch_all()
    payload = []
    for city in cities:
        payload.append({
            'id': city.id,
            'city_name': city.city_name
        })

    return success(payload)

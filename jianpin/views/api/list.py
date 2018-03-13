# -*- coding: utf-8 -*-
from jianpin import app
from jianpin.views.api import success


@app.route('/api/job.list')
def job_list():
    """
    doc/list.md
    :return:
    """

    payload = []

    return success(payload)

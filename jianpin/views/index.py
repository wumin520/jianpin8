# -*- coding: utf-8 -*-
from flask import jsonify

from jianpin import app


@app.route('/')
def welcome():

    return jsonify({'message': 'hello world'})

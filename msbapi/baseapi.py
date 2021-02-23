#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:

    def send_requests(self, req: dict):
        '''
        对requests进行二次封装 解包关键字传参
        :return:
        '''
        return requests.request(**req)

    def jpath(self, obj, j_expr):
        '''
        对jsonpath进行二次封装
        :return:
        '''
        return jsonpath(obj, expr=j_expr)

    def jschema(self, instance, schema):
        '''
        对jsonschema进行二次封装
        :return:
        '''
        return validate(instance, schema)

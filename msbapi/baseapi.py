#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
class BaseApi:

    def send_requests(self, req:dict):
        '''
        对requests进行二次封装 解包关键字传参
        :return:
        '''
        return requests.request(**req)
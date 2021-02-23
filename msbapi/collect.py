#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from msbapi.baseapi import BaseApi


# 关于收藏的接口，增加取消收藏，收藏列表，是否收藏
class Collect(BaseApi):

    def add_collect(self, payload):
        '''
        增加收藏
        :param payload:type和typeid由前端定位数据，格式：payload='type=1&typeid=1'
        :return: "data": {
        "collectid": 4228319}
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com/v5/collect/add",
            "headers":
                {'userid': '5fc5ba8171c97068bc242b72',
                 'Content-Type': 'application/x-www-form-urlencoded'
                 },
            "data": payload
        }
        response = self.send_requests(req)
        return response.json()

    def cancel_collect(self, payload):
        '''
        取消收藏
        :param payload:格式 payload='collectid=4228320'
        :return:
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com/v5/collect/cancel",
            "headers":
                {'userid': '5fc5ba8171c97068bc242b72',
                 'Content-Type': 'application/x-www-form-urlencoded'
                 },
            "data": payload
        }
        response = self.send_requests(req)
        return response.json()

    def collect_list(self):
        '''
        收藏列表接口
        type收藏类型(可传多个)；count每页显示数量不传默认20；offset偏移量分页用，有就下次给接口
        :return:
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com/v5/collect/list",
            "headers":
                {'userid': '5fc5ba8171c97068bc242b72'}
        }
        response = self.send_requests(req)
        return response.json()

    def is_collected(self, payload):
        '''
        是否收藏
        :param payload: 格式payload='type=1&typeid=9'
        :return:"data": {
        "collected": false,
        "collectid": ""}
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com/v5/collect/iscollected",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            "data": payload
        }
        response = self.send_requests(req)
        return response.json()

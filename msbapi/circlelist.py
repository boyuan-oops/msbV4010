#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from msbapi.baseapi import BaseApi


class CircleList(BaseApi):

    def specific_circle_list(self, payload):
        '''
        获取特定桶的帖子列表,data为type数据
        :param payload: 帖子相关对应的type值
        101 首页-学习
        161 圈子-推荐
        162 圈子-报考
        162 圈子-老师
        164 圈子-精华
        165 圈子-少儿
        133 圈子-同城
        191 列表-动漫大神
        192 列表-动漫课程
        :return:
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com//v2/circle/list",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            "data": payload
        }
        response = self.send_requests(req)
        return response.json()

    def get_my_list(self, counts):
        '''
        默认获取个人帖子列表前20条数据（count默认20）
        :return:
        '''
        req = {
            "method": "get",
            "url": f"https://preapi2.meishubao.com/v1/topic/getList?count={counts}",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72'}
        }
        response = self.send_requests(req)
        return response.json()

    def delete_topic(self, payload):
        '''
        删除帖子
        :param payload:payload='topic_id=11007782'
        :return: msg提示删除是否成功
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com/v1/topic/deleteTopics",
            "headers": {
                'Content-Type': 'application/x-www-form-urlencoded'},
            "data": payload
        }
        response = self.send_requests(req)
        return response.json()

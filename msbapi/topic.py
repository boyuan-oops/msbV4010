#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from msbapi.baseapi import BaseApi


class Topic(BaseApi):

    def add_topic(self, payload):
        '''
        添加帖子
        :param payload:text帖子文本内容;category_id分类：1聊一聊，2申请评画，3向老师提问，10老师聊一聊;
        images;videos;subject_id;teacher_id(非必填）
        :return:
        '''
        req = {
            "method": "post",
            "url": "https://preapi2.meishubao.com/v1/topic/addTopics",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72'
            },
            "data": payload
        }
        response = self.send_requests(req)
        return response.json()

    def get_topic_info(self, topic_id):
        '''
        帖子详情
        :return:
        '''
        req = {
            "method": "get",
            "url": f"https://preapi2.meishubao.com//v1/topic/getInfo?topic_id={topic_id}",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72'
            }
        }
        response = self.send_requests(req)
        return response.json()

    def get_topic_list(self):
        '''
        我/他的帖子列表.
        Query:user_id他人的用户ID，支持用户的数字ID或24位字符串ID，建议传数据ID;
        status状态，多个可用逗号隔开。1：通过，2删除，10审核中;count每页条数，默认为20
        :return:
        '''
        req = {
            "method": "get",
            "url": "https://preapi2.meishubao.com/v1/topic/getList",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72'
            }
        }
        response = self.send_requests(req)
        return response.json()

    def get_follow_list(self):
        '''
        关注的帖子列表
        :return:
        '''
        req = {
            "method": "get",
            "url": "https://preapi2.meishubao.com/v1/topic/getFollowList",
            "headers": {
                'userid': '5fc5ba8171c97068bc242b72'
            }
        }
        response = self.send_requests(req)
        return response.json()

    def get_specific_type_list(self, topic_type, user_ids):
        '''
        获取用户特定类型的帖子列表
        Query:ser_ids用户ID，多个请用逗号隔开；type帖子类型：1文本帖、2图片帖、3视频帖
        :return:
        '''
        req = {
            "method": "get",
            "url": f"https://preapi2.meishubao.com//v1/topic/getUserSpecificTypeList?type={topic_type}&user_ids={user_ids}"
        }
        response = self.send_requests(req)
        return response.json()
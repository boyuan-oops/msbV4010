# -*- coding: utf-8 -*-
import requests
from jsonpath import jsonpath


class CircleList:
    #获取个人帖子列表
    def getmylist(self):
        url = "https://preapi2.meishubao.com/v1/topic/getList"
        headers = {
            'userid': '5fc5ba8171c97068bc242b72'
        }
        response = requests.get(url=url, headers=headers)
        r = response.json()
        #获取个人帖子列表的最新帖子的id
        latesttopicid = jsonpath(r, "$..list[0][id]")
        return latesttopicid


    def deletetopic(self, payload):
        url = "https://preapi2.meishubao.com/v1/topic/deleteTopics"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=url, headers=headers,data=payload)
        return response.json()


    # 获取特定桶的帖子列表,data为type数据
    #     帖子相关对应的type值
    #     101 首页-学习
    #     161 圈子-推荐
    #     162 圈子-报考
    #     162 圈子-老师
    #     164 圈子-精华
    #     165 圈子-少儿
    #     133 圈子-同城
    #     191 列表-动漫大神
    #     192 列表-动漫课程
    def specificirclelist(self, data):
        url = "https://preapi2.meishubao.com//v2/circle/list"
        #传入用户id
        headers = {
            'userid': '5fc5ba8171c97068bc242b72',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=url, headers=headers, data=data)
        return response.json()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

import pytest
import requests


class TestAddtopic:
    now_time = datetime.datetime.now()

    # pytest装饰器定义参数名称（以形参形式传入测试方法），值以[(),()]形式
    @pytest.mark.parametrize(
        'msg, payload',
        [
            ('帖子内容不能为空！', {}),
            ('帖子内容不能为空！', {"text": "", "category_id": "1"}),
            ('帖子内容不能少于5个字符！', {"text": "嘿", "category_id": "1"}),
            ('帖子内容不能少于5个字符！', {"text": "嘿嘿%@", "category_id": "1"}),
            ('通信成功', {"text": "哈哈哈哈嘿", "category_id": "1"}),
            ('帖子内容不能大于140个字符！', {
                "text": "111111111011111111101111111110111111111011111111101111111110111111111011111111101111111110111111111011111111101111111110111111111011111111101",
                "category_id": "1"}),
            ('您的帖子正在审核中', {'text': '12345', 'category_id': '1',
                           'images': '[{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}]'}),
            ('您的帖子正在审核中', {'text': '12345', 'category_id': '1',
                           'images': '[{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}, '
                                     '{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}]'}),
            ('您的帖子正在审核中', {'text': '12345', 'category_id': '1',
                           'images': '[{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}, '
                                     '{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}]'}),
            ('帖子内容不能为空！', {"text": "", "category_id": "2"}),
            ('帖子内容不能少于5个字符！', {"text": "hi", "category_id": "2"}),
            ('申请评画必须只能选择一张照片', {"text": "hhhhh", "category_id": "2"}),
            ('申请评画必须只能选择一张照片', {"text": "c_time", "category_id": "2", "images": ""}),
            ('待定', {'text': '12345', 'category_id': '2',
                    'images': '[{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}]'}),
            ('待定', {"text": "12345", "category_id": "2",
                    'images': '[{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"},'
                              '{"image_url": "https://image2.meishubao.com/2021-02-08/3591d031c096474520bad8b502cf9dad.jpg","image_width": "838", "image_height": "1146"}]'})
                ('待定', {'text': '12345', 'category_id': '2', 'videos': '[]'})
                ('待定', {'text': '12345', 'category_id': '2', 'videos': '[]'})
        ]
    )
    def test_addtopic(self, msg, payload):
        # str类型转为Python dict类型data = json.loads(payload)
        url = "https://preapi2.meishubao.com/v1/topic/addTopics"
        headers = {
            'userid': '5fc5ba8171c97068bc242b72'
        }
        response = requests.post(url=url, headers=headers, data=payload)
        print("打印接口返回值：")
        print(response.json())
        assert response.json()["msg"] == msg

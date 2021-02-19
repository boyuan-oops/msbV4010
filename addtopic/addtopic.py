# -*- coding: utf-8 -*-
import requests


class AddTopic:

    def addtopic(self, data):
        url = "https://preapi2.meishubao.com/v1/topic/addTopics"
        headers = {
            'userid': '5fc5ba8171c97068bc242b72'
        }
        response = requests.post(url=url, headers=headers, data=data)
        return response.json()
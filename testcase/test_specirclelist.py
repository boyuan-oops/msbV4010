# -*- coding: utf-8 -*-
from jsonpath import jsonpath

from addtopic.addtopic import AddTopic
from circlelist.specificirclelist import CircleList


class TestCase:

    def test_specirclelist_listdongman(self):
        #增加新帖子
        addtopic = AddTopic()
        payload1 = {
            'text': '192 列表-动漫课程',
            'category_id': '1'
        }
        newtopic = addtopic.addtopic(data=payload1)
        print(newtopic)

        #设置指定桶类型

        #查看指定桶帖子列表
        circlelist = CircleList()
        payload2 = 'type=192'
        listcontent = circlelist.specificirclelist(data=payload2)
        specifictopic = jsonpath(listcontent, "$..topic[content]")
        # print(specifictopic)
        assert "192 列表-动漫课程" in specifictopic

        #删除刚刚新建的帖子
        #payload3是帖子id
        topicid = circlelist.getmylist()
        #从列表[]取出数据
        data = topicid.pop()
        payload3 = f'topic_id={data}'
        deletetopic = circlelist.deletetopic(payload3)
        print(deletetopic)



t= TestCase()
t.test_specirclelist_slearn()


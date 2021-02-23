# -*- coding: utf-8 -*-
from jsonpath import jsonpath

from circlelist.specificirclelist import CircleList


def deletealltopic():
    #获取用户所有帖子
    circlelist = CircleList()
    mylist = circlelist.getmylist()
    #获取所有帖子的ID值
    alltopicid = jsonpath(mylist, "$..id")
    print(alltopicid)
    for eachid in alltopicid:
        #删除帖子
        payload = f"topic_id={eachid}"
        print(payload)
        de = circlelist.deletetopic(payload)
        print(de)

    afterdelete = circlelist.getmylist()
    print(afterdelete)


demo = deletealltopic()

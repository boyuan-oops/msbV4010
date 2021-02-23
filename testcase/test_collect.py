#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from msbapi.collect import Collect


class TestCollect:

    def setup_class(self):
        self.collect = Collect()

    def test_addcollect(self):
        collectlist = self.collect.collect_list()
        listlen = self.collect.jpath(collectlist, "$..total").pop()
        # listlen = jsonpath(collectlist, "$..total").pop()
        print(listlen)
        payload1 = 'type=7&typeid=38'
        newcollect = self.collect.add_collect(payload1)
        newcollectid = self.collect.jpath(newcollect, "$..collectid").pop()
        # newcollectid = jsonpath(newcollect, "$..collectid").pop()
        print(newcollectid)
        #校验各个返回值的类型
        add_collect_schema = json.load(open("./json_schema/add_collect_schema.json"))
        self.collect.jschema(newcollect, add_collect_schema)
        # validate(newcollect, add_collect_schema)

        # collectlist_after = collect.collectlist()
        # listlen_after = jsonpath(collectlist_after, "$..total").pop()
        # print(listlen_after)
        # assert listlen_after == listlen + 1
        #
        # aftercancel = collect.cancelcollect(newcollectid)
        # cancelid = jsonpath(aftercancel, "$..collectid").pop()
        # assert cancelid == newcollectid

    def test_cancelcollect(self):
        pass

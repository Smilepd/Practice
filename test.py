#coding:utf8

import ip_get
import query

#爬取一次IP，每使用100次爬取的IP列表后更新一次IP列表
def fun1():
    i = 0
    while i < float('inf'):
        if i == 0 or i % 100 == 0:
            ip_get.run()
            i += 1
        else:
            query.run()
            i += 1

if __name__ == "__main__":
    fun1()
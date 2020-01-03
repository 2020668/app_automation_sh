# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/2
E-mail:keen2020@outlook.com
=================================

"""

from common.dir_config import TEST_DATA_DIR


def create_counter():

    def increase():         #定义一个还有自然数算法的生成器,企图使用next来完成不断调用的递增

        n = 0

        while True:

            n = n+1

            yield n

    it = increase()        #一定要将生成器转给一个(生成器)对象,才可以完成,笔者第一次做,这里一直出问题,

                                  #一直没解开,看到别人做的才更改完成

    def counter():        #再定义一内函数

        return next(it)  #调用生成器的值,每次调用均自增（
                         #注意：it不要加()括号调用会出错的

    return counter


counter_ = create_counter()

print(counter_(), counter_())


if __name__ == '__main__':
    count_path = "\\count.txt"
    count_file = TEST_DATA_DIR + count_path
    with open(count_file) as f:
        a = f.read()
        print(a, type(a))


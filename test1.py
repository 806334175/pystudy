# num = 10
#
#
# def demo1():
#     a = 11
#     b = 22
#     return a, b
#
#
# def demo2():
#     a = 1
#     b = 2
#
#     [a, b] = [b, a]
#     print(a)
#     print(b)
#     pass
#
#
# def demo3(num_list):
#     num_list.clear()
#     num_list.append("123")
#     num_list.append("456")
#     pass
#
#
# gl_list = [1, 2, 3]
# demo3(gl_list)
# print(gl_list)
#
# str = "  a  b   c   "
# print(str)
# print(str.strip())
# print(str.replace(" ", ""))


# class Sample:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, type, value, trace):
#         print
#         "type:", type
#         print
#         "value:", value
#         print
#         "trace:", trace
#
#     def do_something(self):
#         bar = 1 / 0
#         return bar + 10
#
#
# with Sample() as sample:
#     sample.do_something()


# with open('tete.py') as op:
#     print(op.closed)
#
# print(op.closed)
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def test(value1, value2=None):
    print("%s threading is printed %s, %s" % (threading.current_thread().name, value1, value2))
    time.sleep(0.01)


#     time.sleep(2)


if __name__ == "__main__":
    threadPool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="test_")

    test1 = []
    for i in range(100):
        test1.append(i)
    test2 = []
    for i in range(100):
        test2.append(100 - i)



    threadPool.map(test, test1, test2)
    # 这是运行一次test的参数，众所周知map可以让test执行多次，即一个[]代表一个参数，一个参数赋予不同的值即增加[]的长度如从[1]到[1,2,3]
threadPool.shutdown(wait=True)

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

msg = input()
print(msg)
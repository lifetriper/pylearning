"""
gbk和utf-8，不能直接转化
gbk -> 文字 -> utf8
"""
s = "周a杰伦"
bs1 = s.encode("gbk")
print(bs1)
bs2 = s.encode("utf-8")
print(bs2)
bs = b'\xd6\xdca\xbd\xdc\xc2\xd7'
print(bs.decode("gbk"))

name = "rishav003840"
print(type(name))
# name = "r  i  s  h  a  v  0  0  3  8  4   0"
#         0  1  2  3  4  5  6  7  8  9  10  11

# print(name[n1,n2,n3])   #mtlb: print start from [n1]
#                              and print till [n2-1] but
#                              also skip n3-1 character alternately till [n2-1]

"""
    print start from [n1] character to [n2-1]
"""

"""agar n3=1 then koi character skip nhi karna
        n3=2 then n1 wla character likho uske baad 1 character skip and 1 character print (alternately)
        n3=3 then n1 wla character likho uske baad 2 character skip and 1 character print (alternately)
        n3=4 then n1 wla character likho uske baad 3 character skip and 1 character print (alternately)
"""

print(name[0:10:1])
#output : rishav0038
#bcz [0][1][2][3][4][5][6][7][8][9] = rishav0038

print(name[0:11:1])
#output : rishav00384
#bcz [0][1][2][3][4][5][6][7][8][9][10] = rishav00384

print(name[0:12:1])
#output : rishav003840
#bcz [0][1][2][3][4][5][6][7][8][9][10][11] = rishav003840

print(name[0:11:2])
#output : rsa034
#bcz [0][2][4][6][8][10] = rsa034

print(name[2:11:2])
#output : sa034
#bcz  [2][4][6][8][10] = sa034

print(name[:4])         
#mtlb: it will print from [0] to till [n-1]
#here n=4 therefore, it will print from [0] to [3]
#same as name[0:4]
#output : rish
#bcz [0][1][2][3] = rish


print(name[1:])         
#mtlb: it will not print from [0] to [n-1]
#here n=1 therefore, it will not print [0]
#same as name[1:12]
#output : ishav003840
#bcz [1][2][3][4][5][6][7][8][9][10][11] = ishav003840
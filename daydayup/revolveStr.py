# -*- coding: utf-8 -*-

##旋转字符串 如abcde 输入旋转前面2个字符串 输出为 edcab
##给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，
##如把字符串“abcdef”前面的2个字符'a'和'b'移动到字符串的尾部，使得原字符串变成字符串“cdefab”。
##请写一个函数完成此功能，要求对长度为n的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。
str = 'abcde'

print str[::-1]

#空间复杂度O(n)
def revolve(str,n=1):
    head = str[0:n] 
    tail = str[-n:]
    print head,tail 
    body = str[n:-n]
    newStr = tail + body + head  
    print newStr

#revolve('abcde',2)

##本来想尝试算法的搞成python切片学习了 - -
def revolve2(str):
    print str[2::-1]


revolve2('123456789')
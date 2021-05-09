def longest_repetition(chars):
    if len(chars) == 0 or len(chars) == 1:
        return (chars, len(chars))
    result = [1] * len(chars)
    for left in range(len(chars) - 1):
        for right in range(left + 1, len(chars)):
            if chars[left] == chars[right]:
                result[left] += 1
            else:
                break
    return (chars[result.index(max(result))], max(result))


# 测试用例
print(longest_repetition("aaaabb"))
print(longest_repetition("cbdeuuu900"))
print(longest_repetition(""))
print(longest_repetition('ba'))
print(longest_repetition("bbbaaabaaaa"))
print(longest_repetition("abbbbb"))
print(longest_repetition("aabb"))
print(longest_repetition("a"))

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # 存储历史循环中最长的子串长度
    max_len = 0
    # 判断传入的字符串是否为空
    if s is None or len(s) == 0:
        return max_len
    # 定义一个字典，存储不重复的字符和字符所在的下标
    str_dict = {}
    # 存储每次循环中最长的子串长度
    one_max = 0
    # 记录最近重复字符所在的位置+1
    start = 0
    for i in range(len(s)):
        # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
        if s[i] in str_dict and str_dict[s[i]] >= start:
            # 记录当前字符的值+1
            start = str_dict[s[i]] + 1
            # print start
        # 在此次循环中，最大的不重复子串的长度
        one_max = i - start + 1
        # 把当前位置覆盖字典中的位置
        str_dict[s[i]] = i
        # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
        max_len = max(max_len, one_max)
    return max_len


print(lengthOfLongestSubstring('pwwssffasdf'))


#
#!usr/bin/env python
#encoding:utf-8
'''''
__Author__:沂水寒城
功能：找出来一个字符串中最长不重复子串
'''
def find_longest_no_repeat_substr(one_str):
  '''''
  找出来一个字符串中最长不重复子串
  '''
  res_list=[]
  length=len(one_str)
  for i in range(length):
    tmp=one_str[i]
    for j in range(i+1, length):
      if one_str[j] not in tmp:
        tmp+=one_str[j]
      else:
        break
    res_list.append(tmp)
  res_list.sort(lambda x,y:cmp(len(x), len(y)))
  return res_list[-1]
if __name__ == '__main__':
  one_str_list=['120135435','abdfkjkgdok','123456780423349']
  for one_str in one_str_list:
    res=find_longest_no_repeat_substr(one_str)
    print('{0}最长非重复子串为：{1}'.format(one_str, res))




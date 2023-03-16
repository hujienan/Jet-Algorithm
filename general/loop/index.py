from collections import defaultdict

def can_form_circle(words):
    if len(words) == 0:
        return False

    # 将所有字符串的首字母和末字母存储在两个列表中
    first_letters = [word[0] for word in words]
    last_letters = [word[-1] for word in words]

    # 检查是否存在一个路径，使得所有字符串首尾相接成环
    current = first_letters[0]
    for i in range(len(words)):
        if current in last_letters:
            # 选择一个未使用过的字符串，将其加入环中，并更新当前字符
            j = last_letters.index(current)
            current = first_letters[j]
            last_letters.pop(j)
            first_letters.pop(j)
        else:
            # 不存在以当前字符为首字母的字符串，无法形成环
            return False

    # 所有字符串都被使用过，并且最后一个字符串的末字母与第一个字符串的首字母相同，形成环
    if not first_letters:
        return not last_letters
    if last_letters:
        return last_letters[0] == first_letters[0]
    return False

words = ["aa"]
assert can_form_circle(words) == True, "Should be True"
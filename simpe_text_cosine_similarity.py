import jieba
import math
str1 = "我喜欢看电视，不喜欢看电影。"
str2 = "我不喜欢看电视，也不喜欢看电影。"

# 分词
word_gen1 = jieba.cut_for_search(str1)
word_gen2 = jieba.cut_for_search(str2)
word_list1 = list(word_gen1)
word_list2 = list(word_gen2)

print(" ".join(word_gen1))
print(" ".join(word_gen2))

# 去重取并集
union_list = list(set(word_list1).union(set(word_list2)))
# 计算词频
list1_tf = []
list2_tf = []
for index in range(len(union_list)):
    list1_tf.append(word_list1.count(union_list[index]))
    list2_tf.append(word_list2.count(union_list[index]))


print(list1_tf)
print(list2_tf)

# 计算余弦值
numerator_list = []
for index in range(len(union_list)):
    numerator_list.append(list1_tf[index] * list2_tf[index])

numerator = sum(numerator_list)
denominator = math.sqrt(sum(map(lambda x: x*x, list1_tf))) * math.sqrt(sum(map(lambda x: x*x, list2_tf)))
# 求值
cosin = numerator/denominator

print(cosin)

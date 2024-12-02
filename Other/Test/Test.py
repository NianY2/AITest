from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# 示例字符串
text1 = "我喜欢编程"
text2 = "我热爱编程"

# 使用部分比率算法计算相似度
similarity = fuzz.ratio(text1, text2)
print(f"Similarity: {similarity}")

# 查找最相似的字符串
choices = ["我喜欢编程", "我喜欢音乐", "我很热爱编程"]
best_match = process.extractOne(text2, choices)
print(f"Best Match: {best_match}")
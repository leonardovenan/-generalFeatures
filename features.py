import random
import linecache
#read an arbritary line from a file
def get_answer():
    line_num = random.randint(1, 5)
    answer = linecache.getline("text.txt", line_num)
    return answer.strip()

result = get_answer()

print(result)

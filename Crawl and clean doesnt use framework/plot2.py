with open('clean_data.csv', encoding ='utf-8') as file:
    data = file.read().split('\n')

header = data[0]
students = data[1:]

# xóa học sinh rỗng (ở cuối danh sách)
students.pop()
students.pop(0)

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]
# split each student 
for i in range(len(students)):
    students[i] = students[i].split(",")

num_of_exam_taken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
average = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0] # điểm trung bình của số môn thi
# ví dụ: average[0] thi 0 môn
# average[1] thi 1 môn
# tính trung bình điểm của các bạn thi 0 môn / 1.../11 môn

# lặp qua toàn bộ students
for s in students:
    count = 0
    total = 0
    # lấy điểm của từng (điểm bắt đầu từ s[5])
    for i in range(11):
        if s[i+5] != "-1":
            total += float(s[i+5])
            count += 1
    num_of_exam_taken[count] += 1
    if count!= 0:
        average[count] += total/count # tổng điểm chia số môn


for i in range(12):
    if num_of_exam_taken[i] != 0:
        average[i] = round(average[i]/num_of_exam_taken[i],2)
    
#print(average)

# plot barchart matplotlib

import matplotlib.pyplot as plt
import numpy as np

y_pos = np.arange(12)
x_pos = np.arange(12)

figure, axis = plt.subplots()
plt.bar(x_pos, average)

# set limit for vertical axis
axis.set_ylim(0,10)
plt.xticks(x_pos, y_pos)
axis.set_ylabel('Điểm trung bình')

rects = axis.patches

labels = average

# Make some labels.
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label,
            ha='center', va='bottom')

plt.show()

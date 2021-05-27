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

not_take_exam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#print(students[-1])

# lặp qua toàn bộ students
for s in students:
    # lấy điểm của từng (điểm bắt đầu từ s[5])
    for i in range(5,16):
        if s[i] == "-1":
            # ví dụ toán = s[5] thì tương ứng với no_take_exam[0]
            not_take_exam[i-5]+=1

not_take_exam_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 11):
    not_take_exam_percentage[i] = (not_take_exam[i]*100/total_student)

#print(not_take_exam_percentage)


# plot barchart matplotlib

import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()


y_pos = np.arange(len(subjects))

plt.bar(y_pos, not_take_exam_percentage, align='center', alpha=0.5)
plt.xticks(y_pos, subjects) # lấy tên môn học dựa theo index rồi show lên trục hoành

# set limit for vertical axis
axis.set_ylim(0,100)

plt.ylabel('Phần trăm')
plt.title('Số học sinh bỏ thi hoặc không đăng kí')

# labels cho các cột
rects = axis.patches
# Make some labels.
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label,
            ha='center', va='bottom')

plt.show()


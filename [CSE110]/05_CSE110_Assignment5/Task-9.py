exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
new_dict = {}
user_inp = int(input())
for key, val in exam_marks.items():
    if val >= user_inp:
        new_dict[key] = val
print(new_dict)

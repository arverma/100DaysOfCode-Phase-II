def merge(studentDetails, studentMark, merge_key):
    student_details = {}
    student_marks = {}
    for sd, sm in zip(studentDetails, studentMark):
        key = sd.pop(merge_key)
        student_details[key] = sd

        key = sm.pop(merge_key)
        student_marks[key] = sm

    res = []
    for id, val in student_details.items():
        # Merge three dictionary together
        temp = {**{"studentId": id}, **val, **student_marks[id]}
        res.append(temp)
    return res


if __name__ == '__main__':
    # Test Case 1
    studentDetails = [
        {"studentId": 1, "studentName": 'Sathish', "gender": 'Male', "age": 15},
        {"studentId": 2, "studentName": 'kumar', "gender": 'Male', "age": 16},
        {"studentId": 3, "studentName": 'Roja', "gender": 'Female', "age": 15},
        {"studentId": 4, "studentName": 'Nayanthara', "gender": 'Female', "age": 16},
    ]
    studentMark = [
        {"studentId": 1, "mark1": 80, "mark2": 90, "mark3": 100},
        {"studentId": 2, "mark1": 80, "mark2": 90, "mark3": 100},
        {"studentId": 3, "mark1": 80, "mark2": 90, "mark3": 100},
        {"studentId": 4, "mark1": 80, "mark2": 90, "mark3": 100},
    ]

    # Test Case 2
    array1 = [
        {"id": "abdc4051", "date": "2017-01-24"},
        {"id": "abdc4052", "date": "2017-01-22"}
    ]
    array2 = [
        {"id": "abdc4051", "name": "ab"},
        {"id": "abdc4052", "name": "abc"}
    ]

    output = merge(studentDetails, studentMark, merge_key="studentId")
    [print(a) for a in output]

    output = merge(array1, array2, merge_key="id")
    [print(a) for a in output]

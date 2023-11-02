def students_credits(*args):
    credits_in_progress = 0
    result_dict = {}
    final_message = ''
    for ch in args:
        course, credit, max_result, diyan_result = ch.split("-")
        diyan_credits = 0
        if int(diyan_result) != 0 and int(max_result) != 0:
            diyan_credits = int(credit) / (int(max_result) / int(diyan_result))
        credits_in_progress += diyan_credits
        result_dict[course] = diyan_credits
    if credits_in_progress >= 240:
        final_message += f"Diyan gets a diploma with {credits_in_progress:.1f} credits." + "\n"
    else:
        final_message += f"Diyan needs {240 - credits_in_progress:.1f} credits more for a diploma." + "\n"
    sorted_dict = dict(sorted(result_dict.items(), key=lambda x: -x[1]))
    for course, result in sorted_dict.items():
        final_message += f"{course} - {result:.1f}" + "\n"
    return final_message

print(students_credits("Computer Science-12-300-0"))

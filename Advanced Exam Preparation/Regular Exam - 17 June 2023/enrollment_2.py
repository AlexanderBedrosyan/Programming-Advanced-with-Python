def gather_credits(*args):
    number_of_credits_needed = int(args[0])
    course_information = args[1:]
    enrolled_courses = []
    credits_counter = 0

    if number_of_credits_needed == 0:
        return f"Enrollment finished! Maximum credits: {credits_counter}.\nCourses: {', '.join(enrolled_courses)}"

    for information in course_information:
        course_name = information[0]
        credits = int(information[1])

        if course_name in enrolled_courses:
            continue

        credits_counter += credits
        enrolled_courses.append(course_name)

        if credits_counter >= number_of_credits_needed:
            enrolled_courses = sorted(enrolled_courses, key=lambda x: x)
            return f"Enrollment finished! Maximum credits: {credits_counter}.\nCourses: {', '.join(enrolled_courses)}"
    return f"You need to enroll in more courses! You have to gather {number_of_credits_needed - credits_counter} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

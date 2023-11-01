def forecast(*args):
    correct_way = ["Sunny", "Cloudy", "Rainy"]
    information = {}
    final_info = []
    for ch in args:
        city, weather = ch
        if weather not in information:
            information[weather] = []
        information[weather].append(city)

    for weather in correct_way:
        if weather in information:
            for info in sorted(information[weather]):
                final_info.append(f"{info} - {weather}")
    return '\n'.join(final_info)

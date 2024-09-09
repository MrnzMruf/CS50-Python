#https://cs50.harvard.edu/python/2022/psets/1/meal/


def main():
    timedate_input = input("What time is it? ")
    # if timedate_input.endswith("m"):
    #     print(type(timedate_input))
    #     print(timedate_input)
    #     time_converted_12 = convert_12(timedate_input)
    #     time_converted_12 = float(time_converted_12)
    #     if 7 <= time_converted_12 <= 8:
    #         print("breakfast time")
    #     if 12 <= time_converted_12 <= 13:
    #         print("lunch time")
    #     if 18 <= time_converted_12 <= 19:
    #         print("dinner time")
    #     else:
    #         return 0
    #else:
    time_converted_24 = convert(timedate_input)
    time_converted_24 = float(time_converted_24)
    if 7 <= time_converted_24 <= 8:
        print("breakfast time")
    if 12 <= time_converted_24 <= 13:
        print("lunch time")
    if 18 <= time_converted_24 <= 19:
        print("dinner time")
    else:
        return 0

def convert(timedate_input):
    hours, minutes = timedate_input.split(":")
    time_converted_24 = round(float(hours) + (float(minutes) / 60), 2)
    #return ("{:.2f}".format(time_converted_24))
    return time_converted_24


# def convert(timedate_input):
#     hours, minutes = timedate_input.split(":")
#     minutes = minutes.split(" ")
#     minutes[1] = minutes[1].lower()
#     hours = float(hours)
#     if minutes[1] == "pm" and hours != 12:
#         hours += 11
#     elif minutes[1] == "am" and hours == 12:
#         hours = 0
#     minutes[0] = float(minutes[0])
#     time_converted_12 = round(float(hours) + (float(minutes[0]) / 60), 2)
#     print(f"2 {time_convert}")
#     return time_converted_12

if __name__ == "__main__":
    main()




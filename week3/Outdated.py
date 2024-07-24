def get_month_index(month_name):
    months = [
        "January", "February", "March", "April", "May", 
        "June", "July", "August", "September", 
        "October", "November", "December"
    ]
    try:
        return months.index(month_name) + 1  # Months are 1-indexed
    except ValueError:
        return None

def is_valid_date(date_str):
    # Check if the input is of the form MM/DD/YYYY
    if '/' in date_str:
        parts = date_str.split('/')
        if len(parts) == 3:
            month, day, year = parts
            if month.isdigit() and day.isdigit() and year.isdigit():
                month = int(month)
                day = int (day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    return month, day, year

    # Check if the input is of the form Month Day, Year
    elif ',' in date_str:
        parts = date_str.split(',')
        if len(parts) == 2:
            year = parts[1].strip()
            month_day = parts[0].strip()
            month_day_parts = month_day.split()
            if len(month_day_parts) == 2:
                month_name = month_day_parts[0]
                day = month_day_parts[1]
                if day.isdigit() and (month_index := get_month_index(month_name)) is not None:
                    day = int(day)
                    if 1 <= day <= 31 and year.isdigit() and int(year) > 0:
                        return month_index, day, int(year)
    return None

def format_date_to_iso(month, day, year):
    return f"{year}-{month:02}-{day:02}"

def main():
    while True:
        date_input = input("Date: ")
        valid_date = is_valid_date(date_input)
        if valid_date:
            month, day, year = valid_date
            iso_date = format_date_to_iso(month, day, year)
            print(f"{iso_date}")   # The date in ISO format is: 
            break
        else:
            pass

if __name__ == "__main__":
    main()

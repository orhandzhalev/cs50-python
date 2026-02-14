months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            s = input("Date: ").strip()

            if "/" in s:
                m_str, d_str, y_str = s.split("/")
                month = int(m_str)
                day = int(d_str)
                year = int(y_str)

            else:
                month_name, rest = s.split(" ", 1)
                if month_name not in months:
                    raise ValueError

                day_str, year_str = rest.split(", ")
                month = months.index(month_name) + 1
                day = int(day_str)
                year = int(year_str)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            pass


main()
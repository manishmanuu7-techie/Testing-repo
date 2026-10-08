import calendar
from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def age_calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])

            birth_date = date(year, month, day)
            today = date.today()

            if birth_date > today:
                error = "Your date of birth cannot be in the future."
                return render_template("index.html", result=result, error=error)

            years = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                years -= 1

            birthday_year = birth_date.year + years

            if birth_date.month == 2 and birth_date.day == 29:
                if calendar.isleap(birthday_year):
                    last_birthday = date(birthday_year, 2, 29)
                else:
                    last_birthday = date(birthday_year, 2, 28)
            else:
                last_birthday = date(
                    birthday_year, birth_date.month, birth_date.day
                )

            months = today.month - last_birthday.month
            if today.day < last_birthday.day:
                months -= 1

            if months < 0:
                months += 12

            if today.day >= birth_date.day:
                days = today.day - birth_date.day
            else:
                first_day_this_month = date(today.year, today.month, 1)
                last_month_last_day = (
                    first_day_this_month - date.resolution
                ).day
                days = (last_month_last_day - birth_date.day) + today.day

            total_days = (today - birth_date).days

            result = {
                "birth_date": birth_date.strftime("%d-%m-%Y"),
                "today": today.strftime("%d-%m-%Y"),
                "years": years,
                "months": months,
                "days": days,
                "total_days": total_days,
            }

        except ValueError:
            error = "Please enter a valid date."

        except KeyError:
            error = "Please enter all date fields."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

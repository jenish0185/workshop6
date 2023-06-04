def avg(weekly_temp):
    weekend = []
    for day, temp in weekly_temp.items():
        if day.lower() == 'saturday':
            weekend.append(temp)
        if not weekend:
            return None
        else:
            return sum(weekend)/len(weekend)
temperatures = { 'Sunday':20, 'Monday':24, 'Tuesday':23, 'Wednesday':24, 'Thursday':25, 'Friday':21, 'Saturday':27}
weekend_avg = avg(temperatures)
print(weekend_avg)
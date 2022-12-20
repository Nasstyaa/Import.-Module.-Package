def calculate_salary():
    salary_per_day = int(input('Введите зарплату за один рабочий день: '))
    number_of_days = int(input('Введите количество отработанных за месяц дней: '))
    salary = salary_per_day * number_of_days
    print(f'Зарплата за "{number_of_days}" отработанных дней при зарплате "{salary_per_day}" за один рабочий день равна "{salary}"')


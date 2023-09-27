import json

companies = []
profits = []
try:
    with open("companies.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                name, ownership, revenue, expenses = parts
                revenue = float(revenue)
                expenses = float(expenses)
                profit = revenue - expenses
                profits.append(profit)
                companies.append({name: profit})
except IOError:
    print("Произошла ошибка ввода-вывода!")
average_profit = sum([p for p in profits if p > 0]) / len([p for p in profits if p > 0])
companies.append({"average_profit": average_profit})
try:
    with open("companies.json","w") as json_file:
        json.dump(companies,json_file, ensure_ascii=False, indent=4)
except IOError:
    print("Произошла ошибка ввода-вывода!")


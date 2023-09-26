import json

companies = []
profits = []
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
average_profit = sum([p for p in profits if p > 0]) / len([p for p in profits if p > 0])
companies.append({"average_profit": average_profit})
with open("companies.json","w") as json_file:
    json.dump(companies,json_file, ensure_ascii=False, indent=4)


data = input()
companies = {}

while data != "End":
    company, employee = data.split(" -> ")
    companies[company] = companies.get(company, [])
    if employee not in companies[company]:
        companies[company].append(employee)

    data = input()

for company, employees in companies.items():
    print(f"{company}\n" + '\n'.join([f"-- {worker}" for worker in employees]))

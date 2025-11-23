print("\nIncome and Expense Tracking Program\n")

record_t = []       # t = type of tansaction(income or expense)
record_val = []      # val = amount of transaction(numerical amount)
record_cat = []        # cat = category name

while True:
    entry = input("Type of entry (income / expense). Type 'end' to stop: ").strip().lower()

    if entry == "end":
        print("\nData entry has stopped.\n")
        break

    if entry not in ["income", "expense"]:
        print("Please enter either 'income' or 'expense'.")
        continue

    val = float(input("Enter amount: "))
    cat = input("Enter category name: ")

    record_t.append(entry)
    record_val.append(val)
    record_cat.append(cat)

record_t = np.array(record_t)
record_val = np.array(record_val)
record_cat = np.array(record_cat)

total_in = record_val[record_t == "income"].sum()
total_out = record_val[record_t == "expense"].sum()
balance = total_in - total_out

print("~ Summary ~")
print("Total Income  :", total_in)
print("Total Expense :", total_out)
print("Net Balance   :", balance)

if balance >= 0:
    print("Status: You have saved money.")
else:
    print("Status: Your spending is greater than your earnings.")

plt.figure()
plt.bar(["Income", "Expense"], [total_in, total_out])
plt.title("Overall Income vs Expense")
plt.ylabel("Amount")
plt.show()


expense_vals = record_val[record_t == "expense"]
expense_cats = record_cat[record_t == "expense"]

if expense_vals.size > 0:
    plt.figure()
    plt.pie(expense_vals, labels=expense_cats, autopct="%.2f%%")
    plt.title("Category-wise Expense Distribution")
    plt.show()
else:
    print("No expense entries added, so pie chart will not be shown.")

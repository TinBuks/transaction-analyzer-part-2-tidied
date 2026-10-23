data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_deposited = sum(deposits)
  total_withdrawn = sum(withdrawals)
  balance = total_deposited + total_withdrawn
  print(total_deposited)
  print(total_withdrawn)
  print(balance)

def analyze_transactions(transactions):
  transactions.sort()
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_deposit = sum(deposits)
  total_withdrawals = sum(withdrawals)
  average_deposit = round(total_deposit / len(deposits), 2) if deposits else 0
  average_withdrawal = round(total_withdrawals / len(withdrawals), 2) if withdrawals else 0
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"Largest Withdrawal: {largest_withdrawal}")
  print(f"Largest Deposit: {largest_deposit}")
  print(f"Average Withdrawal: {average_withdrawal}")
  print(f"Average Deposit: {average_deposit}")

while True:
  print("Print Summary, Analyze Transaction, Stop")
  choice = input(" ")
  if choice == "Print Summary" or choice == "print summary":
    print_summary(data)
  elif choice == "Analyze Transaction" or choice == "analyze transaction" or choice == "analyze":
    analyze_transactions(data)
  elif choice == "Stop" or choice == "stop":
    break
  else:
    print("Invalid choice")

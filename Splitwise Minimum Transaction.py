def minTransactions(amounts):
    maxGivingIndex = amounts.index(max(amounts))
    maxOwingIndex = amounts.index(min(amounts))
    
    indexUserMapping = {v: k for k, v in users.items()}
    
    if abs(amounts[maxGivingIndex]) <= 1e-9 and abs(amounts[maxOwingIndex]) <= 1e-9:
        return

    min_amount = min(abs(amounts[maxGivingIndex]), abs(amounts[maxOwingIndex]))
    amounts[maxGivingIndex] -= min_amount
    amounts[maxOwingIndex] += min_amount
    print(f"Person {indexUserMapping[maxGivingIndex]} pays {min_amount} to Person {indexUserMapping[maxOwingIndex]}.")

    minTransactions(amounts)


def splitWiseTransactions(payment_matrix):
    n = len(payment_matrix)
    if n == 0:
        return

    amounts = [0] * n
    for i in range(n):
        for j in range(n):
            amounts[i] += payment_matrix[j][i] - payment_matrix[i][j]

    minTransactions(amounts)



bill_input = [
    {"A": 2000, "B": 200, "C": 1000},
    {"A": 1500, "B": 0, "C": 0, "D": 1300},
    {"B": 100, "C": 0},
]

def calculate_payments(bill_input, users):
    n = len(users)
    payments = [[0] * n for _ in range(n)]

    for entry in bill_input:
        for payer, amount in entry.items():
            payer_index = users[payer]

            if amount > 0:
                split_amount = round(amount / len(list(entry.keys())))
                list(entry.keys())
                for receiver in list(entry.keys()):
                    if(receiver!=payer):
                        receiver_index = users[receiver]
                        payments[receiver_index][payer_index] += split_amount

    return payments

def user_index_mapping(bill_input):
    users = dict()
    index=0
    for entry in bill_input:
        for name in entry.keys():
            if name not in users:
                users[name]=index
                index+=1
    return users
users = user_index_mapping(bill_input)
payment_matrix = calculate_payments(bill_input, users)

splitWiseTransactions(payment_matrix)


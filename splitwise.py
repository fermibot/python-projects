import csv
import sys


def main():
    # Read CSV filename from command line
    if len(sys.argv) != 2:
        print("Usage: python splitwise_app.py <expenses.csv>")
        return

    filename = sys.argv[1]
    expenses = []
    participants = set()

    # Read and parse CSV file
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Parse required fields
                expense = {
                    'paid_by': row['paid_by'],
                    'amount': float(row['amount'])
                }

                # Parse optional paid_for field
                if 'paid_for' in row and row['paid_for'].strip():
                    paid_for = [name.strip() for name in row['paid_for'].split(';')]
                    expense['paid_for'] = paid_for
                    participants.update(paid_for)
                else:
                    expense['paid_for'] = None

                # Parse optional percentages field
                if 'percentages' in row and row['percentages'].strip():
                    percentages = [float(pct.strip()) for pct in row['percentages'].split(';')]
                    expense['percentages'] = percentages

                # Add to expenses
                expenses.append(expense)
                participants.add(expense['paid_by'])

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except KeyError as e:
        print(f"CSV file missing required column: {e}")
        return
    except ValueError as e:
        print(f"Error parsing value: {e}")
        return

    participants = sorted(participants)
    n = len(participants)
    if n == 0:
        print("No participants found.")
        return

    # Initialize gross_debts: debtor -> creditor -> amount
    gross_debts = {p: {q: 0.0 for q in participants} for p in participants}

    # Process each expense
    for expense in expenses:
        paid_by = expense['paid_by']
        amount = expense['amount']

        if 'paid_for' in expense and expense['paid_for'] is not None:
            beneficiaries = expense['paid_for']
        else:
            beneficiaries = participants  # all participants

        if 'percentages' in expense and expense['percentages'] is not None:
            percentages = expense['percentages']
            if len(percentages) != len(beneficiaries):
                print(f"Error: Percentages count doesn't match beneficiaries in expense paid by {paid_by}")
                continue
            shares = [amount * pct / 100.0 for pct in percentages]
        else:
            num_beneficiaries = len(beneficiaries)
            if num_beneficiaries == 0:
                shares = []
            else:
                share_val = amount / num_beneficiaries
                shares = [share_val] * num_beneficiaries

        for i, person in enumerate(beneficiaries):
            if i < len(shares):
                share = shares[i]
                if person != paid_by:
                    gross_debts[person][paid_by] += share

    # Compute net grid: net_grid[debtor][creditor] = net amount debtor owes creditor
    net_grid = {debtor: {} for debtor in participants}
    for debtor in participants:
        for creditor in participants:
            if debtor == creditor:
                net_grid[debtor][creditor] = 0.0
            else:
                debt_forward = gross_debts[debtor][creditor]
                debt_backward = gross_debts[creditor][debtor]
                net_owed = debt_forward - debt_backward
                if net_owed > 0:
                    net_grid[debtor][creditor] = round(net_owed, 2)
                else:
                    net_grid[debtor][creditor] = 0.0

    # Print the grid
    header = "\t" + "\t".join(participants)
    print(header)

    for debtor in participants:
        row = [debtor]
        for creditor in participants:
            amount = net_grid[debtor][creditor]
            row.append("{:.2f}".format(amount))
        print("\t".join(row))


if __name__ == "__main__":
    main()

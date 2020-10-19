import math, argparse, sys


def calc_interest(num):
    return num * 0.01 / 12


def calc_diff_pay(principal, interest, periods, repayment_month):
    return math.ceil((principal / periods)
            + interest
            * (principal - ((principal * (repayment_month - 1)) / periods)))


def calc_principal(payment, periods, interest):
    return (payment / ((interest * (1 + interest) ** periods)
            / ((1 + interest) ** periods - 1)))


def calc_payment(principal, periods, interest):
    return math.ceil(principal
            * (interest * (1 + interest) ** periods)
            / ((1 + interest) ** periods - 1))


def calc_periods(principal, payment, interest):
    periods = math.log(payment / (payment - interest * principal),
                       1 + interest)
    periods = math.ceil(periods)
    num_years = periods // 12
    num_months = periods % 12
    return [num_years, num_months]


def calc_overpay(principal, total):
    return total - principal


parser = argparse.ArgumentParser(description="Calculate loan payment")
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument("--payment", type=int, help="The monthly payment amount")
parser.add_argument("--principal", type=int, help="The initial loan amount")
parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="Interest")

args = parser.parse_args()

# Check if 4 args have been passed (5 including program name)
if len(sys.argv) != 5:
    print("Incorrect parameters.")
    exit()


type_ = args.type                           # which to calculate
payment = args.payment                      # Monthly payment
principal = args.principal                  # Loan principal
periods = args.periods                      # number of payments
interest = calc_interest(args.interest)     # interest rate
calculate = ""

if type_ is None:
    print("Incorrect parameters need type")
    exit()


if type_ == "diff" and payment is None:
    total = 0
    for month in range(1, periods + 1):
        month_pay = calc_diff_pay(principal,
                                  interest,
                                  periods,
                                  month)
        total += month_pay
        print(f"Month {month}: payment is {month_pay}")

    print(f"Overpayment = {calc_overpay(principal, total)}")
    exit()


# find out what to calculate
# by checking if it is not in the arguments passed
# annuity payment
if payment is None:
    payment = calc_payment(principal, periods, interest)
    overpay = calc_overpay(principal, payment * periods)
    print(f"Your annuity payment = {payment}")
    print(f"Overpayment = {overpay}")

# principal loan
if principal is None:
    total = periods * payment

    principal = calc_principal(payment, periods, interest)
    print(f"Your loan principal = {int(principal)}!")
    print(f"Overpayment = {calc_overpay(principal, total)}")

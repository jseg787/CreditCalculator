# CreditCalculator
CreditCalculator project for hyperskill python developer path

Learned to use argparse to create a command line application that calculates loan payment information

## Example use
`python3 creditcalc.py --type=diff --payment=1000 --principal=400000 --interest=0.02`

## Output
```
It will take 33 years and 6 months to repay this loan!
Overpayment 2000
```


## How to use
```
usage: creditcalc.py [-h] [--type {diff,annuity}] [--payment PAYMENT]
                     [--principal PRINCIPAL] [--periods PERIODS]
                     [--interest INTEREST]

Calculate loan payment

optional arguments:
  -h, --help            show this help message and exit
  --type {diff,annuity}
  --payment PAYMENT     The monthly payment amount
  --principal PRINCIPAL
                        The initial loan amount
  --periods PERIODS     The number of months needed to repay the loan
  --interest INTEREST   Interest
```
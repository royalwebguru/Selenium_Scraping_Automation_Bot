import capsolver

CAPSOLVER_API_KEY="CAI-CA8F5D78B888FEB049BE5444950CAA9F"

capsolver.api_key = CAPSOLVER_API_KEY

balance = capsolver.balance()
print(balance)
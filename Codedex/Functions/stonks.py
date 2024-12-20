stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]  
# In this function we only want to return the day with the price 
# (the -1 is there so when we output the function with the day, it represents the right day and not the day after because the index starts at 0)


def max_price(a, b):
  mx = 0  # Initialisiert das Maximum mit 0
  for i in range(a, b + 1):  # Iteriert durch die Tage von 'a' bis 'b' (inklusive)
    mx = max(mx, price_at(i))  # Vergleicht das aktuelle Maximum mit dem Kurs am Tag 'i'
  return mx  # Gibt das höchste gefundene Maximum zurück


def min_price(a, b):
  mn = price_at(a)  # Initialisiert das Minimum mit dem Kurs am Tag 'a'
  for i in range(a, b + 1):  # Iteriert durch die Tage von 'a' bis 'b' (inklusive)
    mn = min(mn, price_at(i))  # Vergleicht das aktuelle Minimum mit dem Kurs am Tag 'i'
  return mn  # Gibt das niedrigste gefundene Minimum zurück

print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))

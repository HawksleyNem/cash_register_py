article_price = 1
prices = []
result = 0

while article_price != 0:
    article_price = int(input("Quel est le prix de votre article : "))
    prices.append(article_price)
    print(prices)

for i in prices[0:]:
    result = result + (i)

print(f"La somme de votre panier est : {result} euros.")
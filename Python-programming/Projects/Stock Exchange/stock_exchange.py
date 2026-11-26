
import pandas as pd
import random

stocks = {
    "Available Stock": ["RamyeonCorp", "abc", "cde", "def", "efg", "fgi"],
    "Price": [1500, 800, 2400, 5000, 9999, 0.40],
    "Volatility": [0.70, 0.40, 0.50, 0.09, 0.35, 0.18]
}

def show_title():
    print()
    print()
    print("-" * 95)
    print(f"                                            STOCK EXCHANGE                            ")
    print()
    print()
    print("Welcome to the Stock Exchange, where you'll learn about stock in a funnier way..")
    print()
    print("The rules here are simplyyy easyyy!")
    print()
    rules = [
        "You start with 10,000 Won.", 
        "Each day, a news headline hits the market and changes the stock prices.",
        "Buy low and sell high. Watch the news and choose wisely.", 
        "The game lasts 20 days. At the end, your net worth decides your rank."]
    for position, rules in enumerate(rules, start=1):
        print(position, ".", rules)  

show_title()

print()

df = pd.DataFrame(stocks)
print(df)

cash = 10,000
day = 1

def show_market(df, cash, day):
    print(f"Day {day} and you have {cash} Won")
    print(df)

    

# ==========================================
# STOCK PORTFOLIO TRACKER
# ==========================================

# Stock Prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 300,
    "NFLX": 500,
    "FB": 350,
    "NVDA": 220,
    "BABA": 200,
    "JPM": 160,
    "V": 230,
    "MA": 360,
    "DIS": 180,
    "PYPL": 270,
    "ADBE": 650,
    "INTC": 55,
    "CSCO": 60,
    "ORCL": 90,
    "CRM": 250,
    "IBM": 140,
    "QCOM": 150,
    "TXN": 190,
    "AVGO": 500,
    "AMD": 100,
    "SHOP": 1500,
    "SQ": 250,
    "TWTR": 70,
    "UBER": 45,
    "LYFT": 30,
    "ZM": 300,
    "SNOW": 250,
    "DOCU": 250,
    "ROKU": 100,
    "PINS": 60
}

portfolio = {}
total_investment = 0

print("=" * 60)
print("          WELCOME TO STOCK PORTFOLIO TRACKER")
print("=" * 60)

# Display available stocks
print("\nAvailable Stock Symbols:")
print(", ".join(stock_prices.keys()))

# Get user input
try:
    n = int(input("\nEnter the number of different stocks you want to buy: "))

    if n <= 0:
        print("Please enter a positive number of stocks.")

    else:
        # Get stock details
        for i in range(n):

            print(f"\nEnter details for Stock {i + 1}")

            stock_symbol = input("Enter stock symbol: ").upper().strip()

            if stock_symbol not in stock_prices:
                print("Invalid stock symbol. Purchase skipped.")
                continue

            try:
                quantity = int(input(
                    f"Enter quantity of {stock_symbol}: "
                ))

                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                    continue

            except ValueError:
                print("Invalid quantity. Purchase skipped.")
                continue

            # Calculate investment
            price = stock_prices[stock_symbol]
            investment = price * quantity

            # Store stock details (supports duplicate stocks)
            if stock_symbol in portfolio:
                portfolio[stock_symbol]["quantity"] += quantity
                portfolio[stock_symbol]["total_investment"] += investment

            else:
                portfolio[stock_symbol] = {
                    "quantity": quantity,
                    "price_per_share": price,
                    "total_investment": investment
                }

            total_investment += investment

            print("Stock added successfully!")

        # ======================================
        # DISPLAY PORTFOLIO SUMMARY
        # ======================================

        print("\n" + "=" * 75)
        print("                    PORTFOLIO SUMMARY")
        print("=" * 75)

        print(
            f"{'Stock Symbol':<15}"
            f"{'Quantity':<12}"
            f"{'Price/Share':<18}"
            f"{'Investment':<15}"
        )

        print("-" * 75)

        for stock_symbol, details in portfolio.items():

            print(
                f"{stock_symbol:<15}"
                f"{details['quantity']:<12}"
                f"${details['price_per_share']:<17}"
                f"${details['total_investment']:<15}"
            )

        print("-" * 75)

        print(f"Total Investment: ${total_investment}")

        # ======================================
        # CURRENT PORTFOLIO VALUE
        # ======================================

        current_portfolio_value = 0

        for stock_symbol, details in portfolio.items():

            current_price = stock_prices[stock_symbol]

            current_value = current_price * details["quantity"]

            current_portfolio_value += current_value

        print(
            f"Current Portfolio Value: "
            f"${current_portfolio_value}"
        )

        # ======================================
        # PROFIT OR LOSS
        # ======================================

        profit_or_loss = (
            current_portfolio_value - total_investment
        )

        print(f"Profit/Loss: ${profit_or_loss}")

        percentage_change = 0

        if total_investment > 0:

            percentage_change = (
                profit_or_loss / total_investment
            ) * 100

            print(f"Percentage Change: {percentage_change:.2f}%")

        # Display final result
        if profit_or_loss > 0:
            print("Congratulations! You made a profit.")

        elif profit_or_loss < 0:
            print("Unfortunately, you incurred a loss.")

        else:
            print("Your portfolio is at break-even.")

        # ======================================
        # FILE HANDLING - WRITE FILE
        # ======================================

        with open("portfolio_summary.txt", "w") as file:

            file.write("=" * 60 + "\n")
            file.write("          STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 60 + "\n\n")

            file.write(
                f"{'Stock Symbol':<15}"
                f"{'Quantity':<12}"
                f"{'Price/Share':<18}"
                f"{'Investment':<15}\n"
            )

            file.write("-" * 60 + "\n")

            for stock_symbol, details in portfolio.items():

                file.write(
                    f"{stock_symbol:<15}"
                    f"{details['quantity']:<12}"
                    f"${details['price_per_share']:<17}"
                    f"${details['total_investment']:<15}\n"
                )

            file.write("-" * 60 + "\n")

            file.write(
                f"\nTotal Investment: ${total_investment}\n"
            )

            file.write(
                f"Current Portfolio Value: "
                f"${current_portfolio_value}\n"
            )

            file.write(f"Profit/Loss: ${profit_or_loss}\n")

            file.write(
                f"Percentage Change: {percentage_change:.2f}%\n"
            )

            if profit_or_loss > 0:
                file.write("Result: Profit\n")

            elif profit_or_loss < 0:
                file.write("Result: Loss\n")

            else:
                file.write("Result: Break-even\n")

        print("\nPortfolio summary saved successfully!")

        # ======================================
        # FILE HANDLING - READ FILE
        # ======================================

        print("\n========== SAVED FILE CONTENT ==========")

        with open("portfolio_summary.txt", "r") as file:
            print(file.read())

        print("Thank you for using Stock Portfolio Tracker!")

except ValueError:
    print("Invalid input! Please enter a valid integer.")

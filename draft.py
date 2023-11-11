from sqlalchemy import func

# Assuming you have an active session object named "session"
asset_symbol_to_filter = "ABC"

# Calculate average buy and sell prices and total amount of shares directly in the database query
query = session.query(
    extract('month', Share.date).label('month'),
    func.avg(case([(Share.share_type == "buy", Share.price)])).label('avg_buy_price'),
    func.avg(case([(Share.share_type == "sale", Share.price)])).label('avg_sell_price'),
    func.sum(case([(Share.share_type == "buy", Share.amount)])).label('total_buy_amount'),
    func.sum(case([(Share.share_type == "sale", Share.amount)])).label('total_sale_amount')
).filter(Share.asset_symbol == asset_symbol_to_filter).group_by(extract('month', Share.date))

# Execute the query and fetch the results
results = query.all()

# Print the average buy and sell prices and total amounts for each month
for result in results:
    month = result.month
    avg_buy_price = result.avg_buy_price or 0
    avg_sell_price = result.avg_sell_price or 0
    total_buy_amount = result.total_buy_amount or 0
    total_sale_amount = result.total_sale_amount or 0

    print(f"Month: {month}, Average Buy Price: {avg_buy_price}, Average Sell Price: {avg_sell_price}, Total Buy Amount: {total_buy_amount}, Total Sale Amount: {total_sale_amount}")

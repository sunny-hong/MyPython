# Design an algorithm that determines the maximum profit that could have been made by buying and then selling a single share over a given day range, subject to the constraint that the buy and the sell have to take place at the start of the day. (Such an algorithm may be needed to backtest a trading strategy.)
def buy_sell_5_6(prices):
  if len(prices) < 1:
    return 0
  
  diff = 0
  # diff : max difference yet
  for buyday in range(len(prices)):
    for sellday in range(buyday, len(prices)):
        if (prices[sellday]-prices[buyday]) > diff:
          diff = prices[sellday]-prices[buyday]
  return diff

# Time O(n^2) Space O(1)

p = [100, 110, 50, 70, 80, 40, 60] 
p2 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
p3 = [310, 315]

#print(buy_sell_5_6(p))
#print(buy_sell_5_6(p2))
#print(buy_sell_5_6(p3))
#print(buy_sell_5_6(p4))

# book's solution
def new_buy_sell(prices):
  if len(prices)<1:
    return 0
  if type(prices) != list:
    return 0

  keep_min, max_diff = float("inf"), 0.0 # infinity

  for price in prices:
    today_diff = price - keep_min
    max_diff = max(max_diff, today_diff)
    keep_min = min(keep_min, price)
  
  return max_diff
# Time O(n)  Spcae O(1)
print(new_buy_sell(p))
print(new_buy_sell(p2))
print(new_buy_sell(p3))
print(new_buy_sell([]))

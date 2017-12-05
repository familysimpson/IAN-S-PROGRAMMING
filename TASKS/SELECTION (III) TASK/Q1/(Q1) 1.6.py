#DECLARE ValidCoin: STRING

print("Input Coin")
ValidCoin = input()

if ValidCoin in ("10", "20", "50", "100"):
    print("TRUE")
else:
    print("FALSE")

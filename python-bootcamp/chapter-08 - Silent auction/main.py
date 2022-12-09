# Silent auction
bids = {}
theresAnotherBidder = True
while theresAnotherBidder:
    name = input('Input your name: ')
    bid = abs(float(input('Input your bid: $')))
    bids[name] = bid
    theresAnotherBidder = input('Is there another bidder? [y/n]: ').lower() == 'y'
print(bids)
max = 0
maxBidder = ''
for bidder in bids:
    if bids[bidder] > max:
        max = bids[bidder]
        maxBidder = bidder

print(f'{maxBidder} wins the auction on price ${max}')

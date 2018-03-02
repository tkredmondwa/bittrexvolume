# bittrexvolume
Snapshots of volume change in Bittrex
A simple script that used Bittrex public API to record volume changes.
Works with Python 2.7. have not tested it with 3.0

Lines 21-165. These are the Bittrex pairs. You may need to update them, since Bittrex adds/removes pairs every now and then. You may get an error 
if Bittrex removes a specific pair.

Line 9. Delay in seconds (15) before the 1st API call. It shows a countdown on screen. If you don't want to see the countdown, erase line 11.

Line 211. Delay in seconds before the next APi call. Default value is 30 seconds. Anything below this value, you may get IP ban from Bittrex. 
Feel free to change it as you see fit. I have found 300 seconds to work well for day trading, but this is all subjective.

How to use it:
Download the bittrexvolume.py file
Open IDLE (Python GUI). Open the bittrexvolume.py file and choose run.

It will show volume in ascending order.

If you change line 258 to
sorted_x = sorted(sortlist.items(), key=operator.itemgetter(1), reverse=True)
the sorting will show decreased volumes first.

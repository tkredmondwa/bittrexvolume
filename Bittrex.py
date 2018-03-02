def runme():	

	# Works only with Python 2.7


	import time

	import sys
	for i in range(15,0,-1): #Countdown in seconds before the first call of public API
	    time.sleep(1)
	    sys.stdout.write(str(i)+' ')
	    sys.stdout.flush()



	import requests
	response = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
	bittrexvolume = response.text # Captures a snapshot of all pairs


	# You may need to update Bittrex pairs, since it adds/removes pairs every now and then
	coins = ["BTC-1ST", 
	"BTC-ABY", 
	"BTC-ADA",
	"BTC-ADT", 
	"BCT-ADX", 
	"BTC-AEON", 
	"BTC-AGRS", 
	"BTC-AMP", 
	"BTC-ANT", 
	"BTC-ARDR", 
	"BTC-ARK", 
	"BTC-BAT", 
	"BTC-BAY", 
	"BTC-BCC",
	"BTC-BITB", 
	"BTC-BLK",
	"BTC-BRK", 
	"BTC-CFI", 
	"BTC-CVC", 
	"BTC-DASH", 
	"BTC-DCR", 
	"BTC-EBST", 
	"BTC-EDG", 
	"BTC-EMC", 
	"BTC-EMC2", 
	"BTC-ETC", 
	"BTC-ETH", 
	"BTC-FCT", 
	"BTC-FLO", 
	"BTC-FUN", 
	"BTC-GAME", 
	"BTC-GBG", 
	"BTC-GBYTE", 
	"BTC-GLD",
	"BTC-GNO", 
	"BTC-GNT", 
	"BTC-GOLOS", 
	"BTC-GRC", 
	"BTC-GRS", 
	"BTC-HMQ",
	"BTC-INCNT", 
	"BTC-INFX", 
	"BTC-IOC", 
	"BTC-ION", 
	"BTC-IOP", 
	"BTC-KMD", 
	"BTC-KORE", 
	"BTC-LBC", 
	"BTC-LGD", 
	"BTC-LMC", 
	"BTC-LSK",
	"BTC-LTC", 
	"BTC-LUN", 
	"BTC-MCO", 
	"BTC-MEME", 
	"BTC-MONA", 
	"BTC-MTL", 
	"BTC-MUE", 
	"BTC-MYST", 
	"BTC-NAV", 
	"BTC-NBT", 
	"BCT-NEO", 
	"BTC-NLG", 
	"BTC-NXC", 
	"BTC-NXS",
	"BTC-NXT", 
	"BTC-OK", 
	"BTC-OMG", 
	"BTC-OMNI", 
	"BTC-PART", 
	"BTC-PAY", 
	"BTC-PDC", 
	"BTC-PINK", 
	"BTC-PIVX", 
	"BTC-PKB", 
	"BTC-POT", 
	"BTC-PPC", 
	"BTC-PTC", 
	"BTC-PTOY", 
	"BTC-QRL", 
	"BTC-QTUM", 
	"BTC-QWARK", 
	"BTC-RADS", 
	"BTC-RBY", 
	"BTC-RDD", 
	"BTC-REP", 
	"BTC-RISE", 
	"BTC-RLC", 
	"BTC-SAFEX", 
	"BTC-SBD", 
	"BTC-SC", 
	"BTC-SEQ", 
	"BTC-SHIFT", 
	"BTC-SIB", 
	"BTC-SLR", 
	"BTC-SLS", 
	"BTC-SNGLS", 
	"BTC-SNRG", 
	"BTC-SNT", 
	"BTC-SPHR", 
	"BTC-SPR", 
	"BTC-START", 
	"BTC-STEEM", 
	"BTC-STORJ", 
	"BTC-STRAT", 
	"BTC-SWIFT",
	"BTC-SWT", 
	"BTC-SYNX", 
	"BTC-SYS", 
	"BTC-THC", 
	"BTC-TIME", 
	"BTC-TKN", 
	"BTC-TKS", 
	"BTC-TRIG", 
	"BTC-TRST", 
	"BTC-TRUST", 
	"BTC-TX", 
	"BTC-UBQ", 
	"BTC-UNB", 
	"BTC-VIA", 
	"BTC-VOX", 
	"BTC-VRC", 
	"BTC-VRM", 
	"BTC-VTC",
	"BTC-VTR", 
	"BTC-WAVES", 
	"BTC-WINGS", 
	"BTC-XAUR", 
	"BTC-XCP", 
	"BTC-XDN", 
	"BTC-XEL", 
	"BTC-XEM", 
	"BTC-XLM", 
	"BTC-XMG", 
	"BTC-XMR", 
	"BTC-XMY", 
	"BTC-XRP", 
	"BTC-XST", 
	"BTC-XVC", 
	"BTC-XVG", 
	"BTC-XZC", 
	"BTC-ZCL", 
	"BTC-ZEC", 
	"BTC-ZEN"]

	counter = len(coins)
	print ("Number of coins ", counter)

	#-------------------------------------------------------------------------
	import re
	# Imports regular expression to be used to search volumes wth decimals

	coinsinitivolumes ={}
	# Empty dictionary of coin-volume pair

	for x in range(0, counter):
		pairposition = bittrexvolume.find(coins[x])
		# Run the loop and find each coin pair.
		newposition = (pairposition + 73)
		# Approximately 95 characters from pair is the value of the volume (24 hours volume)
		coinvolume = bittrexvolume[newposition:newposition+25]
		# Record 25 characters to capture entire volume. Will catch some text as well
		tempcoinvalue = re.findall( r'\d+\.*\d*', coinvolume )
		# Clean text from actual value
		coinvolume = tempcoinvalue
		# Temporary assignment
		tempvaluepairforupdateofdictionary = {coins[x]: coinvolume}
		# Create pair of coin/value
		coinsinitivolumes.update(tempvaluepairforupdateofdictionary)
		# Update dictionary
	#--------------------------------------------------------------
	coinsinitvalues ={}
	for x in range(0, counter):
		coinsinitvalues[x] = (coins[x]+"initvalue")
	# Create initial value of coin pair

	for x in range(0, counter):
		coinsinitvalues[x] = coinsinitivolumes.get(coins[x])
		# Get each coin volume
		converttostring = ''.join(coinsinitvalues[x])
		# Create a sequence
		coinsinitvalues[x] = float(converttostring)
		# Create floating point value
	#--------------------------------------------------------------
	import time
	# Number 300 in line 210 is the number of seconds before the second call of API
	# Do not use values less than 60 (seconds). Bittrex may ban your IP if you do so.

	import sys
	for i in range(30,0,-1):
	    time.sleep(1)
	    sys.stdout.write(str(i)+' ')
	    sys.stdout.flush()
	# # ------------------------------------------------------------
	import requests
	response = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
	bittrexvolume = response.text
	#----------------------------------
	coinsnewvolumes ={}
	# Empty dictionary of coin-volume pair

	for x in range(0, counter):
		pairposition = bittrexvolume.find(coins[x])
		newposition = (pairposition + 73)
		coinvolume = bittrexvolume[newposition:newposition+25]
		tempcoinvalue = re.findall( r'\d+\.*\d*', coinvolume )
		coinvolume = tempcoinvalue
		tempvaluepairforupdateofdictionary = {coins[x]: coinvolume}
		coinsnewvolumes.update(tempvaluepairforupdateofdictionary)
	#----------------------------------------

	coinsaftervalues ={}
	for x in range(0, counter):
		coinsaftervalues[x] = (coins[x]+"aftervalue")

	for x in range(0, counter):
		coinsaftervalues[x] = coinsnewvolumes.get(coins[x])
		converttostring = ''.join(coinsaftervalues[x])
		coinsaftervalues[x] = float(converttostring)
	#---------------------------------------------------------

	changes ={}
	for x in range(0, counter):
		changes[x] = (((coinsaftervalues[x] / coinsinitvalues[x])-1)*100)
	#-----------------------------------------------------------
	highvolumecoin = []

	sortlist ={}
	for x in range(0, counter):
		sortlist[x] = [{'change':changes[x]}, {'coin':coins[x]}]

	#------------------------------------
	import operator
	from operator import attrgetter
	import timeit

	sorted_x = sorted(sortlist.items(), key=operator.itemgetter(1))
	# Use reverse=True for reverse order, lowest volume
	for x in range(0, counter):
		print (sorted_x[x], )


for x in range(0,1000): # Number of times the script runs. 1000 means 1000 X 5 minutes. 
	print x, "times run"
	runme()
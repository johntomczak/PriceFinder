import csv
import urllib2

def prices( today):
	# universally set
	main = "https://www.quandl.com/api/v3/datasets/"
	baseP = ".csv?rows=1&api_key=4rPBKrUryJJ5wJjwfH9Y"

	### SP500
	code = "YAHOO/INDEX_GSPC"
	newP = "&column_index=4"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	inx = list( readr )    						     		 # make "array" - all simplified in following
	inx = inx[1][1]								     		 # make into single value
	inx = round( float( inx ), 2 )							 # str to float, cut to x.xx
	# print inx

	### DJIA - curl "https://www.quandl.com/api/v3/datasets/YAHOO/INDEX_DJI.csv?rows=1&api_key=4rPBKrUryJJ5wJjwfH9Y&column_index=4" -X GET
	code = "YAHOO/INDEX_DJI"
	newP = "&column_index=4"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	response = urllib2.urlopen( main + code + baseP + newP ) # open connection

	readr = csv.reader( response ) 
	lst = list(readr)
	day = lst[1][0]
	dji = round( float( lst[1][1] ), 2 )	 		 # simplified assignment (see SP500)
	print day
	print dji

	### WTI
	code = "CHRIS/CME_CL1"
	newP = "&column_index=6"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	wti = round( float( list( readr )[1][1] ), 2 )   		 # simplified assignment (see SP500)
	# print wti

	### Brent
	code = "CHRIS/ICE_B1"
	newP = "&column_index=6"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	brent = round( float( list( readr )[1][1] ), 2 ) 		 # simplified assignment (see SP500)
	# print brent

	### Gold
	code = "CHRIS/CME_GC1"
	newP = "&column_index=6"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	gold = round( float( list( readr )[1][1] ), 2 )	 		 # simplified assignment (see SP500)
	# print gold

	### VIX
	code = "CBOE/VIX"
	newP = "&column_index=4"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	vix = round( float( list( readr )[1][1] ), 2 )	 		 # simplified assignment (see SP500)
	# print vix

	### loop the Treasuries

	code = "USTREASURY/YIELD"
	govt = [0,0,0,0,0,0,0,0,0,0,0]

	for i in range(0, 11):
		newP = "&column_index=" + str(i+1)
		response = urllib2.urlopen( main + code + baseP + newP ) # open connection
		readr = csv.reader( response )                   		 # recognize CSV
		govt[i] = round( float( list( readr )[1][1] ), 2 )	 	 # simplified assignment (see SP500)

	### construct USDXY - need USD to EUR, JPY, GBP, CAD, SEK, CHF - like the rest

	###### USDEUR
	code = "CURRFX/EURUSD"
	newP = "&column_index=1"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	eur = round( float( list( readr )[1][1] ), 4 )	 		 # simplified assignment (see SP500)

	###### USDJPY
	code = "CURRFX/USDJPY"
	newP = "&column_index=1"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	jpy = round( float( list( readr )[1][1] ), 4 )	 		 # simplified assignment (see SP500)

	###### USDGBP
	code = "CURRFX/GBPUSD"
	newP = "&column_index=1"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	gbp = round( float( list( readr )[1][1] ), 4 )	 # simplified assignment (see SP500)

	###### USDCAD
	code = "CURRFX/USDCAD"
	newP = "&column_index=1"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	cad = round( float( list( readr )[1][1] ), 4 )	 		 # simplified assignment (see SP500)

	###### USDSEK
	code = "CURRFX/USDSEK"
	newP = "&column_index=1"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	sek = round( float( list( readr )[1][1] ), 4 )	 		 # simplified assignment (see SP500)

	###### USDCHF
	code = "CURRFX/USDCHF"
	newP = "&column_index=1"

	response = urllib2.urlopen( main + code + baseP + newP ) # open connection
	readr = csv.reader( response )                   		 # recognize CSV
	chf = round( float( list( readr )[1][1] ), 4 )	 #		  simplified assignment (see SP500)

	###### synthesize the USDXY

	dxy = 50.14348112 * pow(eur, -0.576) * pow(jpy, 0.136) * pow(gbp, -0.119) * pow(cad, 0.091) * pow(sek, 0.042) * pow(chf, 0.036)
	dxy = round( dxy, 4 )


	# print "S&P 500 			=", inx
	# print "DJIA    			=", dji
	# print "WTI     			=", wti
	# print "Brent   			=", brent
	# print "gold    			=", gold
	# print "VIX     			=", vix
	# print "dxy				=", dxy
	# print "Treasury yields  		=", govt

#####
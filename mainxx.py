import prices
import datetime
import time

def run( today ) :
	prices.prices( today )

def main() :
	
	while( 1 == 1 ) :
		weekday = datetime.datetime.now().weekday()
		nw = datetime.datetime.now().time()
		today = datetime.date.today()
		# print weekday, nw, today
		if( weekday < 5 ) :
			if( nw > datetime.time( 16, 05, 30, 0, tzinfo=None ) ) :     # 4.15
				if( nw < datetime.time( 22, 15, 0, 0, tzinfo=None ) ) :	# 6.15
					#this will need to be wrapped in a try / catch
					print "running now", nw
					run( today )
		
		print "waiting 10 minutes from - ", nw
		time.sleep( 600 ) #wait 30 minutes and then sight the window again

######
main()
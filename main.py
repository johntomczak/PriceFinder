import prices
import datetime
import time

def run( today ) :
	prices.prices( today )

def main() :
	i = 1
	while( i == 1 ) :
		weekday = datetime.datetime.now().weekday()
		nw = datetime.datetime.now().time()
		today = datetime.date.today()
		# print weekday, nw, today
		i += 1
		if( weekday < 9 ) :
			if( nw > datetime.time( 16, 25, 0, 0, tzinfo=None ) ) :     # 4.25
				if( nw < datetime.time( 17, 0, 0, 0, tzinfo=None ) ) :	# 5.00
					#this will need to be wrapped in a try / catch
					print "runnning now"
					run( today )
		
		print "waiting"
		# time.sleep( 1800 ) #wait 30 minutes and then sight the window again

######
main()
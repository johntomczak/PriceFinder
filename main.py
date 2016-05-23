import prices
import datetime

def run( today ) :
	prices.prices( today )

def main() :
	i = 1
	while( i<2 ) :
		today = datetime.date.today()
		i+=1

	run( today )

######
main()
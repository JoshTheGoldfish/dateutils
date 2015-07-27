from datetime import date, timedelta

def generate_date_list(start_date, end_date):
	"""Create a range of dates and return it as a list of strings"""
	assert type(start_date) is date 
	assert type(end_date) is date

	tDelta = end_date - start_date

	return [start_date + timedelta(days=i) for i in range(tDelta.days + 1)]

def get_next_days(start_date, days_forward):
	assert type(start_date)   is date
	assert type(days_forward) is int

	return generate_date_list(start_date, start_date + timedelta(days=days_forward))

def dates_for_weekday(dates, day):
	"""Filters the list of dates by a weekday specified (0-6).
	0 is Monday, 6 is Sunday"""
	assert type(day) is int
	
	return [date for date in dates if date.weekday() == day]

###
### Abstractions on top of dates_for_weekday to make code more readable
### Note: these do not currently have tests
###
def get_all_mondays(dates):
	return dates_for_weekday(dates, 0)

def get_all_tuesdays(dates):
	return dates_for_weekday(dates, 1) 

def get_all_wednesdays(dates):
	return dates_for_weekday(dates, 2) 

def get_all_thursdays(dates):
	return dates_for_weekday(dates, 3) 

def get_all_fridays(dates):
	return dates_for_weekday(dates, 4) 

def get_all_saturdays(dates):
	return dates_for_weekday(dates, 5) 

def get_all_sundays(dates):
	return dates_for_weekday(dates, 6) 

def date_of_upcoming_weekday(given_date, weekday):
	"""Returns the date of the weekday closest to given_date where weekday is
	an int 0-6 where 0 represents Monday, and 6 represents Sunday"""
	assert type(given_date) is date
	assert type(weekday)    is int

	return given_date + timedelta(days=days_to_weekday(given_date, weekday))

###
### Abstractions on top of date_of_upcoming_weekday to make code more readable
###	Note: These do not currently have tests
###
def date_of_upcoming_monday(given_date):
	return date_of_upcoming_weekday(given_date, 0)

def date_of_upcoming_tuesday(given_date):
	return date_of_upcoming_weekday(given_date, 1)

def date_of_upcoming_wednesday(given_date):
	return date_of_upcoming_weekday(given_date, 2)

def date_of_upcoming_thursday(given_date):
	return date_of_upcoming_weekday(given_date, 3)

def date_of_upcoming_friday(given_date):
	return date_of_upcoming_weekday(given_date, 4)

def date_of_upcoming_saturday(given_date):
	return date_of_upcoming_weekday(given_date, 5)

def date_of_upcoming_sunday(given_date):
	return date_of_upcoming_weekday(given_date, 6)

def days_to_weekday(given_date, target_weekday):
	"""Returns the ammount of days from the given_date to the target_weekday.
	target_weekday is an int 0-6, where 0 represents Monday, and 6 represents Sunday"""
	assert type(given_date)     is date
	assert type(target_weekday) is int

	return forward_steps_to_target(target_weekday, (0,1,2,3,4,5,6), given_date.weekday())

###
### Abstractions on top of days_to_weekday to make code more readable
###	Note: These do not currently have tests
###
def days_until_monday(given_date):
	return days_to_weekday(given_date, 0)

def days_until_tuesday(given_date):
	return days_to_weekday(given_date, 1)

def days_until_wednesday(given_date):
	return days_to_weekday(given_date, 2)

def days_until_thursday(given_date):
	return days_to_weekday(given_date, 3)

def days_until_friday(given_date):
	return days_to_weekday(given_date, 4)

def days_until_saturday(given_date):
	return days_to_weekday(given_date, 5)

def days_until_sunday(given_date):
	return days_to_weekday(given_date, 6)

def forward_steps_to_target(needle, haystack, start=0):
	"""A needle to search for in a SORTED HAYSTACK OF INTEGERS. It starts the search at the index
	of start. It will return the amount of steps forward from the start of the search
	to the end. If the needle is before the start location, the returned value will be the amount
	of steps foward if the haystack were duplicated. If the needle is at the start position, the
	function will still search forward. If the needle is not in the haystack, returns -1"""
	assert type(needle)   is int
	assert type(haystack) is tuple
	assert type(start)    is int
	assert needle in haystack

	dblStack  = haystack * 2
	abbrStack = dblStack[start:]
	steps     = 0
	found     = False

	if needle not in haystack:
		steps = -1
	else:
		while steps < len(abbrStack) and not found:
			steps += 1
			if abbrStack[steps] == needle:
				found = True

	return steps

def dates_in_week(start_date):
	"""Returns a list of 7 dates from start_date, to 6 days in the future"""
	assert type(start_date) is date

	return generate_date_list(start_date, start_date + timedelta(weeks=1))

def dates_from_start_date(start_date, days_after_start):
	"""Generates a list of dates with from start_date to the amount of days after the start"""
	assert type(start_date)       is date
	assert type(days_after_start) is int

	return generate_date_list(start_date, start_date + timedelta(days=days_after_start))
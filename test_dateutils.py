import unittest
import dateutils
from datetime import date

class TestDateUtilsGenerateDateList(unittest.TestCase):
	"""Tests dateutils.generate_date_list(start_date, end_date)"""
	def setUp(self):
		"""Set up the list of dates to test on"""
		self.dates = dateutils.generate_date_list(date(2015,1,1), date(2015,1,7))

	def test_generate_date_list_returns_list(self):
		"""Make sure generate_date_list returns a list"""
		self.assertIsInstance(self.dates, list)

	def test_generate_date_list_is_all_dates(self):
		"""Make sure everything in the list that generate_date_list
		returns is a date instance"""
		for iter_date in self.dates:
			self.assertIsInstance(iter_date, date)

	def test_genereate_date_list_values(self):
		"""Make sure the values we expect to be in the list that
		generate_date_list returns are in the list, and that the values
		we expect to not be in the list are not included"""
		self.assertIn(date(2015,1,1), self.dates)
		self.assertIn(date(2015,1,7), self.dates)
		self.assertIn(date(2015,1,3), self.dates)

		self.assertNotIn(date(2014,12,31), self.dates)
		self.assertNotIn(date(2015,1,8),   self.dates)

class TestDateUtilsDatesForWeekday(unittest.TestCase):
	"""Test dateutils.dates_for_weekday(dates, day)"""
	def setUp(self):
		"""Set up list of dates to test on"""
		self.init_dates = []
		for day in range(1,15):
			self.init_dates.append(date(2015,1,day)) # 1/1/2015 - 1/14/2015
		self.dates = dateutils.dates_for_weekday(self.init_dates, 3)

	def test_dates_for_weekday_returns_list(self):
		"""Make sure dates_for_weekday returns a list"""
		self.assertIsInstance(self.dates, list)

	def test_dates_for_weekday_is_all_dates(self):
		"""Make sure everything in the list that dates_for_weekday returns
		is a date instance"""
		for iter_date in self.dates:
			self.assertIsInstance(iter_date, date)

	def test_dates_for_weekday_values(self):
		"""Make sure we're getting the expected values, and not unexpected values"""
		self.assertIn(date(2015,1,1), self.dates)
		self.assertIn(date(2015,1,8), self.dates)

		self.assertNotIn(date(2015,1,2),  self.dates)
		self.assertNotIn(date(2015,1,14), self.dates)

class TestDateUtilsDaysToWeekday(unittest.TestCase):
	"""Test dateutils.days_to_weekday(given_date, target_weekday)"""
	def setUp(self):
		"""Set up date to test on"""
		self.thursday = date(2015,1,1)

	def test_days_to_weekday_returns_int(self):
		self.assertIsInstance(dateutils.days_to_weekday(self.thursday, 0), int)

	def test_days_to_weekday_returns_correct_number_of_days(self):
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 4), 1)
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 5), 2)
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 6), 3)
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 0), 4)
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 1), 5)
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 2), 6)
		self.assertEqual(dateutils.days_to_weekday(self.thursday, 3), 7)

class TestDateUtilsDateOfUpcomingWeekday(unittest.TestCase):
	"""Test dateutils.date_of_upcoming_weekday(date, weekday)"""
	def setUp(self):
		"""Set up list of dates to test on"""
		self.date               = date(2015,1,1) #Thursday
		self.upcoming_friday    = dateutils.date_of_upcoming_weekday(self.date, 4)
		self.upcoming_saturday  = dateutils.date_of_upcoming_weekday(self.date, 5)
		self.upcoming_sunday    = dateutils.date_of_upcoming_weekday(self.date, 6)
		self.upcoming_monday    = dateutils.date_of_upcoming_weekday(self.date, 0)
		self.upcoming_tuesday   = dateutils.date_of_upcoming_weekday(self.date, 1)
		self.upcoming_wednesday = dateutils.date_of_upcoming_weekday(self.date, 2)
		self.upcoming_thursday  = dateutils.date_of_upcoming_weekday(self.date, 3)

	def test_date_of_upcoming_weekday_returns_date(self):
		"""Test that date_of_upcoming_weekday returns a date"""
		self.assertIsInstance(self.upcoming_friday, date)

	def test_date_of_upcoming_weekday_returns_correct_day_of_weekday(self):
		"""Teat that date_of_upcoming_weekday returns the correct weekday"""
		self.assertEqual(self.upcoming_friday.weekday(),    4)
		self.assertEqual(self.upcoming_saturday.weekday(),  5)
		self.assertEqual(self.upcoming_sunday.weekday(),    6)
		self.assertEqual(self.upcoming_monday.weekday(),    0)
		self.assertEqual(self.upcoming_tuesday.weekday(),   1)
		self.assertEqual(self.upcoming_wednesday.weekday(), 2)
		self.assertEqual(self.upcoming_thursday.weekday(),  3)

	def test_date_of_upcoming_wekday_returns_correct_date(self):
		"""Test that date_of_upcoming_weekday returns the correct date"""
		self.assertEqual(self.upcoming_friday,    date(2015,1,2))
		self.assertEqual(self.upcoming_saturday,  date(2015,1,3))
		self.assertEqual(self.upcoming_sunday,    date(2015,1,4))
		self.assertEqual(self.upcoming_monday,    date(2015,1,5))
		self.assertEqual(self.upcoming_tuesday,   date(2015,1,6))
		self.assertEqual(self.upcoming_wednesday, date(2015,1,7))
		self.assertEqual(self.upcoming_thursday,  date(2015,1,8))

if __name__ == '__main__':
	unittest.main()
	print('\n')
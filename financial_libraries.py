
# NOTE: QuantLib and Pyfolio need to be installed to run this script.
# For demonstration purposes, I'll outline basic usage, but this won't run without the libraries installed.

# QuantLib: Introduction and basic examples
import QuantLib as ql

# Setting up a basic date and calendar
today_date = ql.Date(17, 9, 2023)
ql.Settings.instance().evaluationDate = today_date
calendar = ql.UnitedStates()

next_business_day = calendar.advance(today_date, ql.Period(1, ql.Days))
print("Next Business Day:", next_business_day)

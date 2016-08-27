# import specail libaries already built in python
import random 
# list of options to select from
possible_activities = ['a', 'b', 'c']

# choice of what are going to do
the_activity = random.choice (possible_activities)

# display the results to the end user
print "possible activities are: " + str(possible_activities) 
print "what we are going to do: " + the_activity

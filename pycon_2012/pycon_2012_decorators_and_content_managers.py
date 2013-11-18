#******************
# My notes and tests
# 
# credits >
# PyCon 2012 - Decorators and Content Managers
# by Dave Brondsema
# https://speakerdeck.com/brondsem/decorators-and-context-managers
#******************
#
# 

#from decorator import decorator
import os

class TryDecorators():

	#@decorator
	def memoize(some_func, *args):
		'decorator for caching a function'
		def check_cache(*args):
			if not hasattr(func, 'results'):
				some_func.results = {}
			if args not in some_func.results:
				some_func.results[args] = some_func(*args)
			return some_func.results[args]
		return check_cache

	@memoize
	def find_user(user_id):
		'query database and load User object'
		return User.m.get(_id=user_id)

# Tests...
c = TryDecorators()
print c.find_user
print c.find_user.__name__
print c.find_user.__doc__


# callable objects - just create an object that has a __call__ method..

class say_something(object):

	def __init__(self, catchphrase):
		self.catchphrase = catchphrase

	def __call__(self):
		print self.catchphrase

just_call = say_something('hello world')
just_call()


# Context Manager
workfile = os.getcwd() + '/workfile' 
with open(workfile) as f:
	for line in f:
		print line.split(' ')

# replace..
try:
	f = open(workfile)
	for line in f:
		print line.split(' ')
finally:
	f.close()

class working_dir(object):
	def __init__(self, new_dir)


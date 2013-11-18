#******************
# my talk notes and tests
#
# credits >
# Pycon 2012 - Transforming code into Beautiful, Idiomatic Python
# by Raymond Hettinger
# @raymondh
# http://pyvideo.org/video/1780/transforming-code-into-beautiful-idiomatic-pytho
# Raymonds rule:
# One logical line of code equals one sentence in English
#******************
#
# 
#

from functools import partial
from itertools import izip
from collections import defaultdict
import argparse
import os


print '#~~ looping over a range of numbers'

for i in [0,1,2,3,4,5]:
	print i**2
	
for i in range(6):
	print i**2

	
print '#~~~ xrange def:'
for i in xrange(6):
	print i**2


	
print '#~~ looping over a collection'
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
	print colors[i]

for color in colors:
	print color


	
print '#~~ looping backwards'

for i in range(len(colors)-1,-1,-1):
	print colors[i]
	
for color in reversed(colors):
	print color


	
print '#~~ looping over a collection and indicies'
for i in range(len(colors)):
	print i, '-->', colors[i]
	
for i, color in enumerate(colors):
	print i, '-->', color
	


print '#~~ looping over two collections'

names = ['raymond', 'rachel', 'mathew']

n = min(len(names), len(colors))
for i in range(n):
	print names[i], '-->', colors[i]
	
for name, color in zip(names, colors):
	print name, '-->', color
	
for name, color in izip(names, colors):
	print name, '-->', color



print '#~~ looping in sorted order'

colors = ['red', 'green', 'blue', 'yellow']	
for color in sorted(colors):
	print color

for color in sorted(colors, reverse=True):	
	print color
	


print '#~~ custom sort order'

def compare_length(c1, c2):
	if len(c1) < len(c2): return -1
	if len(c1) > len(c2): return 1

print sorted(colors, cmp=compare_length)

print sorted(colors, key=len)



print '#~~ call a function until a sentinel value'

f = open('workfile', 'r+')
blocks = []
while True:
	block = f.read(32)
	if block == '':
		break
	blocks.append(block)
	

blocks = []
for block in iter(partial(f.read, 32), ''):
	blocks.append(block)


	
print '#~~ distinguishing multiple exit points in loops'

def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value == tgt:
			found = True
			break
		if not found:
			return -1
		return i

def find(seq, target):
	for i, value in enumerate(seq):
		if value == tgt:
			break
	else:
		return -1
	return i



print '#~~ looping over dictionary keys'

d = {'mathew':'blue', 'rachel': 'green', 'raymond':'red'}

for k in d:
	print k
	
for k in d.keys():
	if k.startswith('r'):
		del d[k]
		
d = {k: d[k] for k in d if not k.startswith('r')}



print '#~~ looping over dictionary keys and values'

for k in d:
	print k, '-->', d[k]
	
for k, v in d.items():
	print k, '-->', v

for k, v in d.iteritems():
	print k, '-->', v
	


print '#~~ construct a dictionary from pairs'

name = ['raymond', 'rachel', 'mathew']
colors = ['red', 'green', 'blue']

d = dict(izip(names, colors))
print 'd1: %s' % d

d = dict(enumerate(names))
print 'd2: %s' % d

colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
	if color not in d:
		d[color]=0
	d[color]+=1

print 'd3: %s' % d	

d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1

print 'd4: %s' % d
	
d = defaultdict(int)
for color in colors:
	d[color] += 1

print 'd5: %s' % d



print 'Grouping with dictionaries - Part1'

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)

print 'd6: %s' % d



print 'Grouping with dic:onaries - Part2'

d={}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)

print 'd7: %s' % d

d = defaultdict(list)
for name in  names:
	key = len(name)
	d[key].append(name)

print 'd8: %s' % d

print 'Is a popitem() atomic?'

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
	key, value = d.popitem()
	print key, '-->', value

print 'd9: %s' % d



print 'Linking dictionarys - python 3'

'''
defaults = {'color':'red', 'user':'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in vars(namespace).items() if v}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

d = ChainMap(command_line_args, os.environ, defaults)

print 'd10: %s' % d
'''


print 'Improving clarity'

p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

fname, lname, age, email = p



print 'update multiple state variables'

def fibonacci(n): 
	x=0
	y=1
	for i in range(n):
		print x 
		t=y 
		y=x+y 
		x=t

def fibonacci(n): 
	x, y = 0, 1
	for i in range(n):
		print x
		x, y = y, x+y



print 'simultaneos state updates'
x = 1
y = 2
dx = 1
dy = 1
t = 3
m = 4
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

x, y, dx, dy = (x + dx * t, y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))


print 'EFFICIENCY'
print 'concatenating strings'

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
	s += ', ' + name
print s

print ', '.join(names)

print 'updating sequences'

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

del names[0]
names.pop(0)
names.insert(0, 'mark')

names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])

del names[0]
names.popleft()
names.appendleft('mark')

print 'using decorators to factorout administrative logic'

def web_lookup(url, saved={}): 
	if url in saved:
		return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

@cache
def web_lookup(url):
	return urllib.urlopen(url).read()

print 'caching decorator'

def cache(func):
	saved = {}
	@wraps(func)
	def newfunc(*args):
		if args in saved:
			return newfunc(*args)
		result = func(*args)
		saved[args] = result
		return result
	return newfunc

print 'Factor out temporary contexts'

old_context = getcontext().copy()
getcontext().prec = 50
print Decimal(355) / Decimal(113)
setcontext(old_context)

with localcontext(Context(prec=50)):
    print Decimal(355) / Decimal(113)


print 'How to open and close files'

f = open('data.txt')
try:
    data = f.read()
finally:
f.close()

with open('data.txt') as f:
    data = f.read()

print 'How to use locks'

# Make a lock
lock = threading.Lock()
# Old-way to use a lock
lock.acquire()
try:
    print 'Critical section 1'
    print 'Critical section 2'
finally:
    lock.release()
# New-way to use a lock
with lock:
    print 'Critical section 1'
    print 'Critical section 2'

print 'Factor out temporary contexts'

try:
    os.remove('somefile.tmp')
except OSError:
    pass
with ignored(OSError):
    os.remove('somefile.tmp')

print 'Context manager: ignored()'

@contextmanager
def ignored(*exceptions):
	try: yield
    except exceptions:
        pass

print 'Factor out temporary contexts'

with open('help.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
		help(pow)

print 'Context manager: redirect_stdout()'

@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fieldobj
    finally:
        sys.stdout = oldstdout

print 'List Comprehensions and Generator Expressions'

result = []
for i in range(10):
s = i ** 2
    result.append(s)
print sum(result)

print sum([i**2 for i in xrange(10)])

print sum(i**2 for i in xrange(10))
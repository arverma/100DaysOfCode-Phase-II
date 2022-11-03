"""
Table
Build
Order
A
Covid
Stream
Aggregation[copy, sschimmel]

Aman
Ranjan
Verma
Question
Description

During
the
Covid
outbreak, a
system
was
implemented
to
allow
hospitals and test
centers
to
report
the
daily
number
of
confirmed
cases
to
a
central
system.Your
team is responsible
to
answer
certain
questions
based
on
the
stream
of
events.

You
may
only
use
the
following
given
operators
of
a
hypothetical
distributed
stream
processing
framework:

filter(filterFunc: T = > Boolean): Stream[T]

Return
a
new
stream
of
type
T
containing
only
the
elements
that
satisfy
a
predicate(a
function
of
type
T
that
returns
either
True or False).

map[U](mapFunc: (T) = > U): Stream[U]

Return
a
new
stream
of
type
U
by
applying
a
function
to
all
elements
of
the
input
stream
of
type
T.

reduceByKey(reduceFunc: (V, V) = > V): Stream[(K, V)]

Return
a
new
stream
by
applying
the
reduce
function
on
all
the
elements
of
type
V in the
stream
having
the
same
key
of
type
K.The
values
for each key are merged using the associative and commutative reduce function.

INPUT
STREAM:

[{
    "city": "Amsterdam",
    "country": "Netherlands",
    "timestamp": "2020-01-01T00:00:00",
    "new_cases": 1200,
    "reporter": "AMS01"
}, {
    "city": "Amsterdam",
    "country": "Netherlands",
    "timestamp": "2020-01-01T10:00:00",
    "new_cases": 1300,
    "reporter": "AMS02"
}, {
    "city": "Amsterdam",
    "country": "Netherlands",
    "timestamp": "2020-01-01T12:00:00",
    "new_cases": 1400,
    "reporter": "AMS01"
}, {
    "city": "Utrecht",
    "country": "Netherlands",
    "timestamp": "2020-01-01T00:00:00",
    "new_cases": 100,
    "reporter": "UTR01"
}]

Example.Find
the
list
of
Dutch
cities
present in the
stream.

stream.filter(lambda x: x["country"] == "Netherlands")
.map(lambda x: element(key=x["city"], value=x) // make
the
city
the
key
of
the
elements
    .reduceByKey(lambda x, y: x) // in this
case, it
doesn
't matter which element to choose
    .map(lambda x: x["city"]) // format
the
output
to
only
include
the
city
names
Result:

[
    "Amsterdam",
    "Utrecht"
]

Compute
the
following:

A.The
daily
number
of
cases
per
reporter.

[{
     "city": "Amsterdam",
     "country": "Netherlands",
     "date": "2020-01-01",
     "new_cases": 1300,
     "reporter": "AMS02"
 }, {
     "city": "Amsterdam",
     "country": "Netherlands",
     "date": "2020-01-01",
     "new_cases": 1400,
     "reporter": "AMS01"
 }, {
     "city": "Utrecht",
     "country": "Netherlands",
     "date": "2020-01-01",
     "new_cases": 100,
     "reporter": "UTR01"
 }]

B.Total
number
of
cases
per
city and date.

[{
     "city": "Amsterdam",
     "country": "Netherlands",
     "date": "01-01-2020",
     "total_cases": 2700
 }, {
     "city": "Utrecht",
     "country": "Netherlands",
     "date": "01-01-2020",
     "total_cases": 100
 }]

C.For
each
day,
return the
top
most
infected
city
per
country.

D.For
each
month,
return the
top
5
infected
cities
per
country.

123456789101112131516171418


def covid_stream_agg():
    strem = strem.map(lambda x: element(key=(x["reporter"], x["date"]), value=x["new_cases"])).
    reduceBykey(lambda x, y: x[0], (max(x[1]), y))


if __name__ == '__main__':
    covid_stream_agg()

Line: 14
Col: 51
Python
3
Input
Output
Console

Run
Code
Chat
Window

res, ``` res ```,, hint
"""
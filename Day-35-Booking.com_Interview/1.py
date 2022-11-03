"""
A
Table
Build
Order
Covid
Stream
Aggregation[copy, sschimmel]

Aman
Ranjan
Verma
Question
Description

As
part
of
a
job
submission
to
a
server, that is responsible
for orchestrating the creation of tables for consumption by reports, a piece of metadata is submitted that declares the dependencies of the various tables for the given job.It is the responsibility of the server to make sure that a correct build order is chosen and executed.

An
example
of
such
a
dependency
declaration is:

{
    "TableA": ["TableB", "TableC"],
    "TableC": ["TableD"],
    "TableD": ["TableB"]
}
The
above
declaration
states
the
following:

The
are
4
tables in the
job.These
are: TableA, TableB, TableC, and TableD.
TableA
depends
on
TableB and TableC.This
means
that
TableB and TableC
must
be
produced
before
TableA.
TableC
depends
on
TableD.This
means
that
TableD
must
be
created
before
TableC.
TableD
depends
on
TableB.This
means
that
TableB
must
be
created
before
TableD.

In
this
particular
case
a
possible
build
order
for this problem is: TableB, TableD, TableC, TableA.This
means
that
tables
with no dependencies appear first, followed by tables that are dependent on them and ending with the table that has no dependents.In this case, TableB has only dependents, and no dependencies.TableA has only dependencies, and no dependents.

REQUIREMENT

Your
task is to
produce
a
correct
build
order
for a given job submission.

123456789101112131415161718192021
fptr.close()

Autocomplete
Ready
Line: 61
Col: 17
Python
3
Input
Output
Console

Run
Tests

Run
Code
Compiled
Successfully.But
no
test
case
passed.

Test
case
0
Compiler
Message
Wrong
Answer
Input(stdin)
3
TableA
TableB
TableC
TableC
TableD
TableD
TableB
Your
Output(stdout)

Download
TableB
TableD
TableD
TableB
Expected
Output
~ no
response
on
stdout
~
Debug
output

Download
TableC
TableD
TableD

Chat
Window

res, ``` res ```,, hint
"""
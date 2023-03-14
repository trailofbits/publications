# CVE-2022-35737

Integer overflow in SQLite3 `sqlite3_str_vappendf` function.

CVSS 7.5 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H

CVE-2022-35737 was introduced in SQLite version 1.0.12 and fixed in release
3.39.2, available on July 21, 2022. It is exploitable on 64-bit systems, and
exploitability depends on how the program is compiled: arbitrary code execution
is confirmed when the library is compiled without stack canaries, but
unconfirmed when stack canaries are present; denial-of-service is confirmed in
all cases.

Large string inputs to the `sqlite3_str_vappendf` function can cause signed
integer overflow when the format specifier is `%q`, `%Q`, or `%w`. This can
cause user-controlled data to be written beyond the bounds of a stack-allocated
buffer, resulting in program crash, infinite loop, or possible arbitrary code
execution.

This directory contains proof-of-concept code that demonstrates the
exploitation of the vulnerability.

## Proofs-of-Concept

### `snprintf-good-example.c`

Demonstrates that `sqlite3_snprintf` correctly escapes all existing single-quote
characters and adds a leading and trailing single quote to a short string.

Expected outcome:

```
$ ./snprintf-good-example
src: hello, 'world'!
dst: 'hello, ''world''!'
```

### `snprintf-crash.c`

Demonstrates that `sqlite_snprintf` crashes when called with sufficiently large
strings.

Expected outcome: SIGSEGV

```
$ ./snprintf-crash
Segmentation fault (core dumped)
```

### `snprintf-control-pc.c`

Demonstrates that it is possible to control the length of the buffer overflow to
overwrite targeted data on the stack, like the stack canary and saved return
address.

Expected outcome: SIGABRT

```
$ ./snprintf-control-pc
*** stack smashing detected ***: terminated
Aborted (core dumped)
```

### `snprintf-livelock.c`

Demonstrates that it is possible to cause the vulnerable program to loop nearly
endlessly (2^64 iterations).

Expected outcome: loop endlessly (on a reasonable timescale)

```
$ ./snprintf-livelock
<no output>
^C
```

### `pdo-sqlite3-quote-poc.php`

Demonstrates that CVE-2022-35737 is reachable from the PHP interpreter when run
with non-default memory limits.

Expected outcome: SIGSEGV

```
$ php pdo-sqlite3-quote-poc.php
Segmentation fault (core dumped)
```

## Dockerfile

If desired, the proofs-of-concept can be executed in a Docker container that
has dependencies pinned to the vulnerable version of the SQLite library.

```
$ docker build -t cve-2022-35737 .
$ docker run -it --rm cve-2022-35737 /bin/bash
root@289cef859649:/poc# LD_PRELOAD=/sqlite3/build-optimized/.libs/libsqlite3.so ./snprintf-crash
Segmentation fault (core dumped)
```

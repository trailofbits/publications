LIBS=-lsqlite3

.PHONY: all clean

all: snprintf-crash snprintf-control-pc snprintf-livelock snprintf-good-example

snprintf-crash: snprintf-crash.c
	$(CC) -o $@ $^ $(LIBS)

snprintf-control-pc: snprintf-control-pc.c
	$(CC) -o $@ $^ $(LIBS)

snprintf-livelock: snprintf-livelock.c
	$(CC) -o $@ $^ $(LIBS)

snprintf-good-example: snprintf-good-example.c
	$(CC) -o $@ $^ $(LIBS)

clean:
	$(RM) snprintf-crash snprintf-control-pc snprintf-livelock snprintf-good-example

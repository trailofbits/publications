#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>

#define STR_LEN ((0x100000001 - 3) / 2)

int main(int argc, char *argv[]) {

    char *src = calloc(1, STR_LEN + 1); // Account for NULL byte.
    if (!src) { return -1; }
    memset(src, 'a', STR_LEN);

    char *dst = calloc(1, STR_LEN + 3); // Account for extra quotes and NULL byte
    if (!dst) { return -1; }

    sqlite3_snprintf(2*STR_LEN + 3, dst, "'%q'", src);

    printf("src: %s\n", src);
    printf("dst: %s\n", dst);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>

int main(int argc, char *argv[]) {

    char src[] = "hello, \'world\'!";
    char dst[sizeof(src) + 4];  // Add 4 to account for extra quotes.

    sqlite3_snprintf(sizeof(dst), dst, "'%q'", src);

    printf("src: %s\n", src);
    printf("dst: %s\n", dst);
    return 0;
}

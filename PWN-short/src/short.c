#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>
int main() {
	void *addr = mmap(0, 0x1000, 2, 34, 0, 0);	
	read(0, addr, 9);
	mprotect(addr, 0x1000, 5);
	((void (*)(void))addr)();
}

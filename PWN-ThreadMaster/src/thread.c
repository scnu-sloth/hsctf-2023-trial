#include<stdio.h>
#include <pthread.h>
#include <fcntl.h>

void init() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

struct file_obj{
    char blank[0x40];
    pthread_mutex_t lock;
    int fd;
    char name[32];
    char content[0x100];
    int flag;
};
typedef struct file_obj file_obj;

const char* file_name_map[2] = {"flag", "tmp"};
file_obj *file_pool[2] = {0};

size_t read_long() {
    char buf[16];
    read(0, buf, 16);
    return atoi(buf);
}

file_obj* make_file(int idx) {
    if(file_pool[idx]) return file_pool[idx];
    int fd = open(file_name_map[idx], O_RDONLY);
    file_obj* file = (file_obj*)calloc(1, sizeof(file_obj));
    // printf("debug malloc %d -> %p\n", idx, file);
    read(fd, file->content, 0x100);
    close(fd);
    file->flag = (idx == 0) ? 0 : 7;
    file->fd = idx;
    strncpy(file->name, file_name_map[idx], 31);
    file_pool[idx] = file;
    return file;
}

void free_file(int idx) {
    if(file_pool[idx] == 0) return 0;
    // printf("debug free %d\n", idx);
    free(file_pool[idx]);
    file_pool[idx] = 0;
}

void read_file(file_obj* file) {
    if(!(file->flag & 1)) {
        free_file(file->fd);
        printf("%s read Error. Permission Denied\n", file->name);
        return 0;
    }
    // printf("debug read %d -> %p\n", file->fd, file);
    pthread_mutex_lock(&file->lock);
    // printf("debug read begin %d -> %p\n", file->fd, file);
    sleep(6);
    printf("%s\n", file->content);
    pthread_mutex_unlock(&file->lock);
    free_file(file->fd);
}

void write_file(file_obj* file) {
    if(!(file->flag & 2)) {
        free_file(file->fd);
        printf("%s write Error. Permission Denied\n", file->name);
        return 0;
    }
    pthread_mutex_lock(&file->lock);
    sleep(6);
    // printf("debug %s\n", file->name);
    pthread_mutex_unlock(&file->lock);
    free_file(file->fd);
}

void menu_1(){
    puts("1. read");
    puts("2. write");
    puts("3. close");
    putchar('>');
}

void menu_2(){
    puts("0. ./flag");
    puts("1. ./tmp");
    putchar('>');
}


int main() {
    init();
    int* p =malloc(0x200);
    while (1)
    {   
        menu_1();
        size_t op = read_long();
        menu_2();
        unsigned int fd = read_long();
        if(fd >= 2) {
            printf("Error file id\n");
            continue;
        }
        if(op == 1) {
            pthread_t th;
            file_obj* file = make_file(fd);
            pthread_create(&th, NULL, read_file, file);
        } else if(op == 2) {
            pthread_t th;
            file_obj* file = make_file(fd);
            pthread_create(&th, NULL, write_file, file);
        } else if(op == 3) {
            free_file(fd);
        } else {
            printf("Error Op\n");
        }
    }
    
}
CC = gcc
CFLAGS = -Wall
SRCS = mal1.c statistics.c
OBJS = $(SRCS:.c=.o)

all: myprogram.exe

myprogram.exe: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	del /Q $(OBJS) myprogram.exe

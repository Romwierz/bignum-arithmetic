CC = gcc
CFLAGS = -MMD -g -std=gnu17 -fdiagnostics-color=always

APP := main
SRC := $(wildcard *.c)
OBJ := $(SRC:.c=.o)
# DEP := $(OBJ:.o=.d)

all: $(APP)

$(APP): $(OBJ)
	$(CC) $^ $(CFLAGS) -lm -o $@

%.o: %.c
	$(CC) $< -c $(CFLAGS) -o $@

asan:
	$(MAKE) CFLAGS="$(CFLAGS) -fsanitize=address -fno-omit-frame-pointer"
 
clean:
	rm -f $(APP) $(OBJ) $(DEP)

.PHONY: all clean asan

.DELETE_ON_ERROR:

# -include $(DEP)

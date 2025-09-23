CODE = contest2/main.cc
DEBUG_FLAGS = -o0  -Wall -Werror 
TEST_FLAGS = -o0
SRC = 
CC = g++
BUILD = build

debug_n_run:
	$(CC) $(DEBUG_FLAGS) $(CODE) $(SRC) -o $(BUILD)/res
	./$(BUILD)/res

debug:
	$(CC) $(DEBUG_FLAGS) $(CODE) $(SRC) -o $(BUILD)/res

test:
	$(CC) $(TEST_FLAGS) $(CODE) $(SRC) -o $(BUILD)/res


valgrind:
	valgrind ./$(BUILD)/res 1000 12

clean:
	rm -rf $(BUILD)


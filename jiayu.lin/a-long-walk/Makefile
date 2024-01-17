# Define the compiler
CXX = clang++

# Define any compile-time flags
CXXFLAGS = -Wall -g -std=c++17

# Define any directories containing header files
INCLUDES = 

# Define any libraries to link into executable
LFLAGS = 

# Define the source files
SRCS = main.cpp walk.cpp

# Define the object files 
OBJS = $(SRCS:.cpp=.o)

# Define the executable file 
MAIN = myprogram

.PHONY: depend clean

all:    $(MAIN)
	@echo  Simple compiler named myprogram has been compiled

$(MAIN): $(OBJS) 
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $(MAIN) $(OBJS) $(LFLAGS)

.cpp.o:
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<  -o $@

clean:
	$(RM) *.o *~ $(MAIN)

depend: $(SRCS)
	makedepend $(INCLUDES) $^

# DO NOT DELETE THIS LINE -- make depend needs it

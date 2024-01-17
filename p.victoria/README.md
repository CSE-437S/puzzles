## Victoria Prisco
# A Long Walk
To run, execute `python3 a_long_walk.py <input_file>.txt`, the result will be printed to the console. 

One note is that on my computer, using argv, the input file is the 2nd (index 1) argument, but I have run into situations before that the input file is the 1st (?) argument (index 0). If this happens, the code should work with changing line 3 to:
`file = sys.argv[0]`
So sorry if it doesn't work without making this change, but I really don't know why that happens and how I could fix it!
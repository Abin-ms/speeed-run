f1 = open("C:/speed_run/python/filereadandwrite/texxt.txt",'r')
# print(f1.readable()) checks whether we can acces / read the file.
# print(f1.readline()) output - abin readLine() reads only one time and stops reading at the end of that line 
# print(f1.readline()) output - jibin
# print(f1.readline()) output - sulu
# print(f1.readline()) output - sisu
# print(f1.readlines()) # output - ['abin\n', 'jibin\n', 'sulu\n', 'sisu'] :  reads the entire file as a list , each line as each element in the list.
# print(f1.readlines()[1])
for lines in f1.readlines():
    print(lines)
f1.close()
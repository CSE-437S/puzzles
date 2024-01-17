import sys

path = sys.argv[1]
file = open(path, 'r')
total = 0
while True:
    content = file.readline()
    if not content:
        break
    #actual process of doing this
    first = content[0:1]
    second = content[2:3]
    match first:
        case "A":
            match second:
                case "X":
                    total+=1
                    total+=3
                case "Y":
                    total+=2
                    total+=6
                case "Z":
                    total+=3
                    
                    
        case "B":
            match second:
                case "X":
                    total+=1
                    
                case "Y":
                    total+=2
                    total+=3
                case "Z":
                    total+=3
                    total+=6 
                   
        case "C":
             match second:
                case "X":
                    total+=1
                    total+=6
                case "Y":
                    total+=2
                case "Z":
                    total+=3
                    total+=3
            
    
print(f"You have a total score of {total}")    
file.close()
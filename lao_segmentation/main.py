from sys import argv
from sys import exit

input = ""
output = ""


def main():

    try:
        if len(argv) < 3:
            print("Input file is required.")
            global output
            if  output == "":
                output = "output.txt"
            print("e.g: python main.py input.txt output.txt")
            exit(0)

        
        output = argv[2]
        global input; input = argv[1]

        

    except Exception as e:
        print(e)
    



    

        





if __name__ == "__main__":
    main()
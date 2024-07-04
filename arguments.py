import argparse

def cl_arguments():
    parser = argparse.ArgumentParser(description="Welcome to passive v1.0.0")
    parser.add_argument("-map", dest="Map", help="Get picture location")
    parser.add_argument("-steg", dest="Stegno", help="Read Stegnogram")
    arguments = parser.parse_args()
    if not(arguments.Map or arguments.Stegno):
        print("Please specify either -map or -steg and picture to get it from.\n")
    return arguments

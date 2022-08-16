#!/usr/bin/python3
import fetchPrice


filename = "urls.txt"




urls = []


def getURLS():
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        line = line.replace("\n", "")
        line = line.replace("http:", "https:")
        urls.append(line)


getURLS()
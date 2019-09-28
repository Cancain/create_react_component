def isTypeScript():
    ansver = input("tsx or js? ")
    if ansver == "tsx":
        return ".tsx"
    if ansver == "js":
        return ".js"
    else:
        return ""


componentName = input("Name of coponent? ")
fileExtension = isTypeScript()

while fileExtension == "":
    print("try again ")
    fileExtension = isTypeScript()

filename = componentName + fileExtension
f = open(filename, "w+")
f.write("import React from 'react'\n\n")
exportLine = "export default function {}".format(componentName)
f.write(exportLine + "()" " {\nreturn()\n}")

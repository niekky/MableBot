listz = []
count = 0
while True:
    print("---------------------")
    print("You did : ",count)
    #Structure
    data = {
        "tag":"",
        "patterns":[],
        "responses":[]
    }
    #Tag
    print("Tag :")
    tag = input()
    data["tag"] = tag
    print("Patterns (type aa to stop):")
    #Pattern
    while True:
        pattern = input()
        if pattern == "aa": break
        data["patterns"].append(pattern)
    #Responses
    print("Patterns (type aa to stop):")
    while True:
        response = input()
        if response == "aa": break
        data["responses"].append(response)
    listz.append(str(data).replace("\'","\""))
    print("---------------------")
    print(str(listz)[1:-1].replace("\'",""))
    count += 1
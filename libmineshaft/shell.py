import libmineshaft.lang as lang


def run():
    while True:
        response = input("Mineshaft~$ ")
        file = open(".libms_history",  "a")
        rfile = open(".libms_history",  "r")
        wfile = open(".libms_history",  "w")
        if len(rfile.readlines()) >= 1000:
            wfile.write("")
        
        lines = list(rfile.readlines())
        lines.insert(0,  response)
        
        file.writelines(lines)
        file.close()
        lang.respond(response)

import libmineshaft.lang as lang

HISTORYFILE = ".libms_history"

def run():
    while True:
        response = input("Mineshaft~$ ")
        file = open(HISTORYFILE, "a")
        rfile = open(HISTORYFILE, "r")
        wfile = open(HISTORYFILE, "w")
        if len(rfile.readlines()) >= 1000:
            wfile.write("")

        lines = list(rfile.readlines())
        lines.insert(0, response)

        file.writelines(lines)
        file.close()
        lang.respond(response)

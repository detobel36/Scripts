import requests
import time
import re
from sys import argv
from tkinter import filedialog as fdialog
import tkinter as t
import webbrowser as wb

MAX_SIZE = 2000

def correctWithBonPatron(text):
    url = "http://bonpatron.com/ajax"
    params = {"isAjax": "true", "origTime": int(time.time()), "docLang": "fr", "iLang": "fr", "sex": "m", "isL1": 1, "spellchecker": "", "typedText": text, "referer": "http://bonpatron.com/"}

    response = requests.post(url, params=params)
    match = re.search('.*?<text>(.*?)<\/text>.*?<summary>(.*?)<\/summary>.*?<mark>(.*?)<\/mark><words>(.*?)<\/words', response.text)

    return match.group(1)

def getTwoThousandLetterLaTex(latexFile):
    with open(latexFile,'r') as f:
        text = ""
        for line in f:
            line = removeLaTeX(line)
            if len(line.strip()) > 0:
                for word in line.split():
                    if len(text + word) > MAX_SIZE-10: # Ajout d'une marge de manoeuvre
                        sentence = text.split(".")
                        text = sentence[-1]
                        yield ".".join(sentence[:-1]) + "."
                    text += word + " "
                text += "\n"

def removeLaTeX(text):
    # vspace
    removeRegex = '(\\\documentclass\[[\w,]*\]\{[\w]*\})' + '|' + \
                  '(\\\\(setcounter)\*?(\[[\w,\{\}\=\+\-\.\\\]*\])?\{[\w,]*\}\{[\w,]*\})' + '|' + \
                  '(\\\\(usepackage|usetikzlibrary|pagestyle|thispagestyle|fancyhf|rhead|vfill|hfill|enlargethispage|newenvironment|setcounter|vspace)\*?(\[[\w,\{\}\=\+\-\.\\\]*\])?(\{[\w,0-9\.]*\})?)' + '|' + \
                  '(\\\\(parindent|parskip)[0-9\.]+e(m|x))' + '|' + \
                  '(\\\(makeindex|frontmatter|huge|par|pagebreak|fill|newpage|null|large|linebreak|tableofcontents|mainmatter|centering))' + '|' + \
                  '(\\\\(begin|end)(\[[\w,\{\}\=\+\-\.\\\]*\])?\{(document|center|verbatim|titlepage|flushright)\})' + '|' + \
                  '(\\\\(begin|end)\{(figure|itemize|tikzpicture)\}(\[[\w,\{\}\=\+\-\.\\\]*\])?)' + '|' + \
                  '(\\\\(label)\{[\w\_\-\:]*\})' + '|' + \
                  '(\\\\(draw|node).*)'


    text = re.sub(removeRegex, '', text.strip(), flags=re.I)
    text = re.sub('\\\\item', '-', text.strip(), flags=re.I)
    text = re.sub('\$[\w0-9\.\,\-\|\\\\ ]*\$', '\[CODE\]', text.strip(), flags=re.I)
    text = re.sub('(\\\\(ref|cite)\{[\w\_\-\:]*\})', "'x'", text.strip(), flags=re.I)
        
    oldText = ""
    while(oldText != text):
        oldText = text
        match = re.search('(.*)?\\\\(textbf|chapter|caption|textit|footnote|((sub(sub)?)?section))\{(.*)\}(.*)?', text.strip())
        if(match):
            text = ""
            if(len(match.group(1)) > 0):
                text = match.group(1)
            text += match.group(6) + match.group(7)

    oldText = ""
    while(oldText != text):
        oldText = text
        match = re.search('(.*)?\\\\(verb)\|(.*)\|(.*)?', text.strip())
        if(match):
            text = match.group(1) + '"' + match.group(3) + '"' + match.group(4)

    text = re.sub('\%(.*)', '', text.strip())
    text = re.sub('\\\\\\\\', '', text.strip())
    text = re.sub('~:', ' :', text.strip())
    text = re.sub('(~-~)|(~-)|(-~)', ' - ', text.strip())
    text = re.sub('\{\s*\}', '', text.strip())


    return text


def createAndOpenHtmlFile(content, fileName):
    fichier = open(fileName, "w")
    # Header HTML
    htmlContent = "<html><head>"
    htmlContent += '<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>'
    htmlContent += "<style>span.ver{ color: red; font-weight: bold; } span.spellmod{ color: orange; font-weight: bold; } div.hover{ display: none; position: absolute; border: 1px gray solid; padding: 5px;max-width: 500px;z-index: 10; background-color: rgb(255, 252, 252);} body { margin-bottom: 100px;}</style>"
    htmlContent += '<body><div class="hover"></div>'
    htmlContent += content
    htmlContent += '<script>function hoverShow() {$(".hover").show();if($(this).attr("org-title") == undefined) {$(this).attr("org-title", $(this).attr("title"));$(this).attr("title", \'\');}$(".hover").html($(this).attr("org-title"));$(".hover").css("top", $(this).position().top + 30);$(".hover").css("left", $(this).position().left);}function hoverHide() {$(".hover").hide();}$("span.ver").hover(hoverShow, hoverHide);$("span.spellmod").hover(hoverShow, hoverHide);console.log("Script Loaded");</script>'
    htmlContent += "</body></html>"
    fichier.write(htmlContent)
    fichier.close()

    wb.open("http://bonpatron.com", new=2)
    time.sleep(1)
    wb.open(fileName, new=2)



def printHelpFunc(programName):
    print("Command: 'python3 " + programName + " <param>'")
    print("\t<Empty>\t\t\t\tIf you don't select any param, a tkinter file browser will open")
    print("\t-h/--help\t\t\tOpen this help")
    print("\t<LaTexFile>\t\t\tLaTeX input file")
    print("\t<LaTexFile> <outputFile>\tSelect Input and output file")


if __name__ == '__main__':
    fichier = None
    outputFile = "result.html"
    if(len(argv) > 1):
        if(argv[1] in ["--help", "-help", "--h", "-h"]):
            printHelpFunc(argv[0])
        else:
            fichier = argv[1]

        if(len(argv) > 2):
            outputFile = argv[2]

    else:
        root = t.Tk()
        fichier = fdialog.askopenfilename(defaultextension=".tex", title="Open LaTeX file", \
                                        filetypes=[('LaTeX','*.tex'), ('Fichier texte', '*.txt')])
        root.destroy()


    if(fichier != None and len(fichier) > 0 and fichier != ""):
        print("Open file: '" + str(fichier) + "'")

        resultHtml = ""
        first = True
        print("Chargement: ", end="")
        for textSend in getTwoThousandLetterLaTex(fichier):
            print(".", end="")
            if(not first):
                time.sleep(3)
                first = False
            resultHtml += correctWithBonPatron(textSend)
        createAndOpenHtmlFile(resultHtml, outputFile)
            

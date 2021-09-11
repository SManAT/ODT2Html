import subprocess
from subprocess import Popen, PIPE, STDOUT
import sys
import re

# Function to get system clipboard contents


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

# Function to put data on system clipboard


def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()


# Get Markdown copied to clipboard
input_text = getClipboardData()

# Popen pandoc shell command
p = Popen(['pandoc', '-f', 'markdown', '-t', 'latex',
          '--wrap=preserve'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

# Pass Markdown text to pandoc through stdin and get raw LaTeX from pandoc
latex = p.communicate(input=input_text)[0]

# Clean LaTeX:
latex = re.sub(r'\\tightlist\n', r'', latex)  # remove \tightlist
# join \item with its text on a single line; also put tabs in front of \item
latex = re.sub(r'\\item\n\s+', r'\t\\item ', latex)
latex = re.sub(r'\\label.*', r'', latex)  # remove all LaTeX labels

setClipboardData(latex)

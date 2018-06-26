#!/usr/bin/python3

from termcolor import colored as c
#from libs.encryption import *
from libs.console import Autocomplete, start_shell
import config
from getpass import getpass
import time

author = config.info()

help_menu = '''
HELP_MENU_PLACEHOLDER
''' # will add some day

# Pretty colored messages
def error(msg): return "%s %s" % (c("[!]","red"),msg)
def info(msg): return "%s %s" % (c("[*]","cyan"),msg)
def fail(msg): return "[%s] : %s" % (c("FAILED","red"),msg)
def ok(msg): return "[  %s  ] : %s" % (c("OK","green"),msg)
def done(msg): return "[ %s ] : %s" % (c("DONE","green"),msg)

class Handler(object):
        commands = "help ,banner ,exit ".split(",")
        def handle(self,cmd):
                try:
                        base = cmd.split(" ")[0]
                except:
                        base = cmd
                if base == "help":
                        print(help_menu) #make
                        return None
                elif base == "exit":
                        #exit_sequence()
                        return "exit"
                elif base == "banner":
                        print_banner()
                        return None
                else:
                        print(error("Command not found / Invalid syntax"))
                        return None


def print_banner():
        with open("libs/logo.txt","r") as btxt:
                logo = c(btxt.read(),"blue")
                name = author.name
                github = author.github
                print(logo + "\n\tAuthor: %s\n\tGithub: %s" % (
                        c(name,"green"),
                        c(github,"green")))





def start_sequence():
        print_banner()
        time.sleep(1.5)

def main():
        start_sequence() #add to
        start_shell(Handler())

if __name__ == "__main__":
        main()

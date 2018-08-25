import argparse, requests, sys, threading
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="The base URL to test")
parser.add_argument("-w", "--wordlist", help="Wordlist to test")
parser.add_argument("-t", "--threads", type=int, help="Amount of threads to use")
args = parser.parse_args()
def menu():
    if int(args.threads) > 0:
        if args.url[-1] != "/":
            url = args.url + "/"
        else:
            print("")
        print("Trying wordlist %s on %s" % (args.wordlist, args.url))
        with open(args.wordlist, "r") as i:
            for line in i:
                finurl = url + line
                r = requests.get(finurl)
                if r.status_code != 404:
                    print(finurl)
                    print(r.status_code)
    else:
        print("Non-Positive amount of threads, try again!")
        exit()
menu()

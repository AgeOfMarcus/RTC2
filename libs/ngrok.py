import os, time
from subprocess import Popen, PIPE

# Download
def download_64bit():
        os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip > /dev/null")
        os.system("unzip ngrok-stable-linux-amd64.zip > /dev/null")
        os.system("rm ngrok-stable-linux-amd64.zip > /dev/null")
def download_32bit():
        os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null")
        os.system("unzip ngrok-stable-linux-386.zip > /dev/null")
        os.system("rm ngrok-stable-linux-386.zip > /dev/null")
def download_arm():
        os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null")
        os.system("unzip ngrok-stable-linux-arm.zip > /dev/null")
        os.system("rm ngrok-stable-linux-arm.zip")

# Run and kill
def run_ngrok(service="http",port=1029):
        os.system("./ngrok %s %s > /dev/null &" % (service, str(port)))
        time.sleep(10)
        return get_url()

#def get_url():
#        os.system('''echo $(curl -s localhost:4040/inspect/http | grep -oP "window.common[^;]+" | sed "s/^[^\(]*(\"//" | sed "s/\")\s*$//" | sed "s/\\\"/\"/g") | jq -r \".Session.Tunnels | values | map(.URL) | .[]" | grep "^https:" > /tmp/ngrok.url''')
#        with open("/tmp/ngrok.url","r") as f:
#                url = f.read()
#        os.system("rm /tmp/ngrok.url")
#        return url

def get_url():
        return Popen("bash ./libs/ngrok_url.sh",stdout=PIPE,shell=True).communicate()[0].decode()

def kill_ngrok():
        os.system("pkill -f \"ngrok\"")



def time_sleep(secs):
        waited = 0
        old = time.time()
        while True:
                if waited >= 10:
                        break
                new = time.time()
                waited += (new - old)
                old = new

import requests, os, time

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
def run_ngrok(service="http",port=8080):
        os.system("ngrok %s %s > /dev/null &" % (service, str(port)))
        time.sleep(10)
        os.system("curl http://localhost:4040/status | grep \"https://*.ngrok.io\" > ngrok.url")
        fd = open("ngrok.url","r")
        url = fd.read()
        fd.close()
        return url
def kill_ngrok():
        os.system("ps all | grep ngrok > ps.txt")
        time.sleep(0.5)
        fd = open("ps.txt","r")
        res = fd.read()
        fd.close()
        res = res.split("\t")
        pid = res[1]
        os.system("kill -9 %s > /dev/null &" % pid)




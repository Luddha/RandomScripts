from subprocess import call

start_cmd = ["C:\\Program Files\\Oracle\\VirtualBox\\vboxmanage.exe", "startvm"]

pen_boxes = {'kali': 'Kali-Linux-2017.3-vbox-amd64', 'xp': 'win32_xp', 'pf': 'pfsense'}


for i in pen_boxes:
    print("[*] starting vm: " + pen_boxes[i])
    start_cmd.append(pen_boxes[i])
    call(start_cmd, shell=True)
    start_cmd.pop()
import os
import platform

masks = {
0: 4294967294,
1: 2147483646,
2: 1073741822,
3: 536870910,
4: 268435454,
5: 134217726,
6: 67108862,
7: 33554430,
8: 16777214,
9: 8388606,
10: 4194302,
11: 2097150,
12: 1048574,
13: 524286,
14: 262142,
15: 131070,
16: 65534,
17: 32766,
18: 16382,
19: 8190,
20: 4094,
21: 2046,
22: 1022,
23: 510,
24: 254,
25: 126,
26: 62,
27: 30,
28: 14,
29: 6,
30: 2,
31: 0,
32: 1
}

def ping_subnet(subnet):
    if platform.system().lower() == "windows":
        ping_cmd = f"ping -n 1 -w 1 {subnet}"
    else:
        ping_cmd = f"ping -c 1 -W 1 {subnet}"
    response = os.system(ping_cmd)
    return response == 0

def find_open_subnets(net, mask):
    for i in range(0, masks[mask]):
        qwe = str(net[0]) + '.' + str(net[1]) + '.' + str(net[2]) + '.' + str(net[3])
        subnet = qwe
        if ping_subnet(subnet):
            f = open("ips.txt",'a')
            f.write(subnet + '\n')
            f.close()
        if net[3] < 255:
            net[3] += 1
        elif net[2] < 255:
            net[2] += 1
            net[3] = 0
        elif net[1] < 255:
            net[1] += 1
            net[2] = 0
            net[3] = 0
        elif net[0] < 255:
            net[0] += 1
            net[1] = 0
            net[2] = 0
            net[3] = 0
        else:
            print("Айпи превысило 255.255.255.255")
            break
    return 

  

def cycle():
    s = input('Введите сеть и маску:\n') 
    if '/' not in s:
        print('Нет маски')
        return
    
    mask = int(s[s.find('/')+1::])
    net = s[0:s.find('/')]
    net_list = list(map(int, net.split('.')))

    if len(net_list) != 4:
        print('Не существует сети ' + net)
        return
    
    for i in net_list:
        if i > 255 or i < 0:
          print(f'В сети не может быть {i}')
          pass
        
    find_open_subnets(net_list, mask)
  

while True:
  cycle()

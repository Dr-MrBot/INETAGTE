#!/usr/bin/env python3
import os
import time
import random
import sys
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from colorama import init, Fore, Back, Style
import requests
from tqdm import tqdm

# Initialize colorama
init()

# API Key configuration
VALID_API_KEY = "hypercoder"  # Plain API key for comparison
ENCRYPTION_KEY = b'YourVerySecretKey123'  # Key for encryption
TELEGRAM_LINK = "https://t.me/your_telegram_username"  # Replace with your Telegram link

def generate_encryption_key():
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'HyperSecretSalt123',
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(ENCRYPTION_KEY))
    return key

def show_main_menu():
    clear_screen()
    print_banner()
    print(f"\n{Fore.CYAN}[*] Main Menu:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Start Tool")
    print("2. Purchase API Key")
    print("3. Exit{Style.RESET_ALL}")
    
    choice = input(f"\n{Fore.GREEN}[?] Select option (1-3): {Style.RESET_ALL}")
    return choice

def show_api_purchase():
    clear_screen()
    print_banner()
    print(f"\n{Fore.CYAN}[*] API Key Purchase Information{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] To purchase an API key, please contact us on Telegram{Style.RESET_ALL}")
    print(f"\n{Fore.GREEN}[+] Telegram: {TELEGRAM_LINK}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] API Key Features:{Style.RESET_ALL}")
    print("  - Full access to all features")
    print("  - Premium support")
    print("  - Regular updates")
    print("  - Custom wordlist support")
    print(f"\n{Fore.RED}[!] Price: Contact for pricing{Style.RESET_ALL}")
    
    input(f"\n{Fore.GREEN}[?] Press Enter to return to main menu...{Style.RESET_ALL}")
    return show_main_menu()

def load_wordlist(wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}[!] Error loading wordlist: {str(e)}{Style.RESET_ALL}")
        return None

def validate_api_key():
    print(f"\n{Fore.CYAN}[*] API Key Validation Required{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] This tool requires a valid API key to operate{Style.RESET_ALL}")
    
    attempts = 3
    while attempts > 0:
        api_key = input(f"\n{Fore.GREEN}[?] Enter API Key: {Style.RESET_ALL}")
        if api_key == VALID_API_KEY:
            print(f"\n{Fore.GREEN}[+] API Key validated successfully!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Initializing secure environment...{Style.RESET_ALL}")
            for _ in tqdm(range(50), desc="Securing", ncols=75):
                time.sleep(0.05)
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"{Fore.RED}[!] Invalid API Key. {attempts} attempts remaining.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Maximum attempts exceeded. Access denied.{Style.RESET_ALL}")
                print(f"{Fore.RED}[!] Tool will now terminate.{Style.RESET_ALL}")
                sys.exit(1)
    return False

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = f"""
{Fore.RED}██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ████████╗███████╗
{Fore.RED}██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ╚══██╔══╝██╔════╝
{Fore.RED}██║██╔██╗ ██║█████╗     ██║   ███████║██║  ███╗   ██║   █████╗  
{Fore.RED}██║██║╚██╗██║██╔══╝     ██║   ██╔══██║██║   ██║   ██║   ██╔══╝  
{Fore.RED}██║██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝   ██║   ███████╗
{Fore.RED}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
{Fore.YELLOW}                    [ Advanced Instagram Security Tool ]
{Fore.CYAN}                    [ Professional Edition v2.0 ]
{Fore.RED}                    [ Authorized Access Only ]
{Style.RESET_ALL}
"""
    print(banner)

def show_menu():
    print(f"\n{Fore.CYAN}[*] Attack Configuration:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Advanced SSH Attack Mode")
    print("2. Multi-Proxy Chain Attack")
    print("3. Distributed Network Attack")
    print("4. Advanced Settings")
    print("5. Start Attack")
    print("6. Network Configuration")
    print("7. Security Analysis")
    print("8. Load Custom Wordlist{Style.RESET_ALL}")
    
    choice = input(f"\n{Fore.GREEN}[?] Select attack mode (1-8): {Style.RESET_ALL}")
    return choice

def configure_advanced_ssh():
    print(f"\n{Fore.CYAN}[*] Advanced SSH Configuration:{Style.RESET_ALL}")
    ssh_ports = ["22", "2222", "22222", "44444", "55555"]
    print(f"{Fore.YELLOW}Available SSH ports: {', '.join(ssh_ports)}")
    port = input(f"Select SSH port [{ssh_ports[0]}]: {Style.RESET_ALL}") or ssh_ports[0]
    
    print(f"\n{Fore.YELLOW}[*] SSH Encryption Options:{Style.RESET_ALL}")
    print("1. RSA-4096")
    print("2. ED25519")
    print("3. ECDSA-384")
    enc_choice = input(f"Select encryption type [1]: {Style.RESET_ALL}") or "1"
    
    print(f"\n{Fore.GREEN}[+] Using SSH port: {port} with encryption: {enc_choice}{Style.RESET_ALL}")
    return f"SSH-{port}-ENC{enc_choice}"

def configure_multi_proxy():
    print(f"\n{Fore.CYAN}[*] Multi-Proxy Chain Configuration:{Style.RESET_ALL}")
    proxy_types = ["SOCKS5", "HTTP", "HTTPS", "TOR", "I2P"]
    chains = []
    
    for i in range(3):
        print(f"\n{Fore.YELLOW}Proxy Chain Level {i+1}:{Style.RESET_ALL}")
        print(f"Available types: {', '.join(proxy_types)}")
        proxy_type = input(f"Select proxy type [{proxy_types[0]}]: {Style.RESET_ALL}") or proxy_types[0]
        chains.append(proxy_type)
    
    print(f"\n{Fore.GREEN}[+] Configured proxy chain: {' -> '.join(chains)}{Style.RESET_ALL}")
    return " -> ".join(chains)

def configure_network():
    print(f"\n{Fore.CYAN}[*] Network Configuration:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Enable TOR routing")
    print("2. Configure VPN endpoints")
    print("3. Set custom DNS servers")
    print("4. Configure traffic routing")
    print("5. Back to main menu{Style.RESET_ALL}")
    
    choice = input(f"\n{Fore.GREEN}[?] Select option (1-5): {Style.RESET_ALL}")
    if choice in ["1", "2", "3", "4"]:
        print(f"\n{Fore.GREEN}[+] Network configuration updated{Style.RESET_ALL}")
        time.sleep(1)
    return choice

def security_analysis():
    print(f"\n{Fore.CYAN}[*] Running Security Analysis...{Style.RESET_ALL}")
    
    checks = [
        "Checking network encryption...",
        "Analyzing proxy security...",
        "Verifying connection integrity...",
        "Scanning for vulnerabilities...",
        "Testing connection speed...",
        "Validating security protocols..."
    ]
    
    for check in checks:
        print(f"{Fore.YELLOW}[*] {check}{Style.RESET_ALL}")
        for _ in tqdm(range(50), desc="Progress", ncols=75):
            time.sleep(0.05)
        print(f"{Fore.GREEN}[+] Check completed{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}[+] Security analysis completed successfully{Style.RESET_ALL}")

def simulate_loading():
    stages = [
        ("Initializing attack vectors", 100),
        ("Establishing secure connection", 50),
        ("Configuring proxy chain", 75),
        ("Testing network latency", 40),
        ("Bypassing security measures", 60),
        ("Optimizing attack parameters", 45)
    ]
    
    for stage, iterations in stages:
        print(f"\n{Fore.GREEN}[*] {stage}...{Style.RESET_ALL}")
        for _ in tqdm(range(iterations), desc="Progress", ncols=75):
            time.sleep(0.03)

def configure_wordlist():
    print(f"\n{Fore.CYAN}[*] Wordlist Configuration:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Use default wordlist")
    print("2. Load custom wordlist")
    print("3. Generate custom wordlist")
    print("4. Back to main menu{Style.RESET_ALL}")
    
    choice = input(f"\n{Fore.GREEN}[?] Select option (1-4): {Style.RESET_ALL}")
    
    if choice == "1":
        return None
    elif choice == "2":
        wordlist_path = input(f"\n{Fore.GREEN}[?] Enter wordlist path: {Style.RESET_ALL}")
        return load_wordlist(wordlist_path)
    elif choice == "3":
        print(f"\n{Fore.YELLOW}[*] Wordlist Generation Options:{Style.RESET_ALL}")
        print("1. Common passwords")
        print("2. Custom pattern")
        print("3. Back{Style.RESET_ALL}")
        gen_choice = input(f"\n{Fore.GREEN}[?] Select option (1-3): {Style.RESET_ALL}")
        if gen_choice == "1":
            return [
                "P@ssw0rd2024!", "Str0ngP@ss123", "C0mpl3x!ty2024",
                "S3cur3P@ssw0rd", "H@ck3rPr00f!", "Brut3F0rc3!2024",
                "P@ssw0rdM@n@g3r", "S3cur1ty!2024", "C0mpl3xP@ss!",
                "Str0ng!2024", "H@ck3r!2024", "Brut3F0rc3!",
                "hypercoder2024"
            ]
        elif gen_choice == "2":
            pattern = input(f"\n{Fore.GREEN}[?] Enter pattern (use {username} for target username): {Style.RESET_ALL}")
            return [pattern.replace("{username}", username) for username in ["admin", "user", "test"]]
    return None

def simulate_attack(username, attack_mode, custom_wordlist=None):
    if custom_wordlist:
        passwords = custom_wordlist
    else:
        passwords = [
            "P@ssw0rd2024!", "Str0ngP@ss123", "C0mpl3x!ty2024",
            "S3cur3P@ssw0rd", "H@ck3rPr00f!", "Brut3F0rc3!2024",
            "P@ssw0rdM@n@g3r", "S3cur1ty!2024", "C0mpl3xP@ss!",
            "Str0ng!2024", "H@ck3r!2024", "Brut3F0rc3!",
            "hypercoder2024"
        ]
    
    print(f"\n{Fore.YELLOW}[*] Starting {attack_mode} attack on: {username}{Style.RESET_ALL}")
    print(f"{Fore.RED}[!] Warning: This operation may be monitored{Style.RESET_ALL}\n")
    
    for i, password in enumerate(passwords, 1):
        print(f"{Fore.CYAN}[*] Attempt {i}/{len(passwords)}: {password}{Style.RESET_ALL}")
        time.sleep(0.5)
        
        if password == "hypercoder2024":
            print(f"\n{Fore.GREEN}[+] Access granted: {password}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Security bypass successful{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Access granted to account: {username}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Extracting account data...{Style.RESET_ALL}")
            time.sleep(2)
            print(f"{Fore.GREEN}[+] Data extraction complete{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Email: {username}@gmail.com{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Phone: +1-XXX-XXX-XXXX{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Last login: {time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[!] Access denied{Style.RESET_ALL}")
    
    if password != "hypercoder2024":
        print(f"\n{Fore.RED}[!] Operation completed - Access denied{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Total attempts: {len(passwords)}{Style.RESET_ALL}")

def main():
    while True:
        choice = show_main_menu()
        
        if choice == "1":
            clear_screen()
            print_banner()
            
            # Validate API key first
            if not validate_api_key():
                continue
            
            while True:
                attack_mode = "Direct"
                menu_choice = show_menu()
                
                if menu_choice == "1":
                    attack_mode = configure_advanced_ssh()
                elif menu_choice == "2":
                    attack_mode = configure_multi_proxy()
                elif menu_choice == "3":
                    attack_mode = "Distributed Network"
                elif menu_choice == "4":
                    print(f"\n{Fore.CYAN}[*] Advanced Settings:{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}1. Enable deep packet inspection")
                    print("2. Configure custom wordlists")
                    print("3. Enable stealth mode")
                    print("4. Configure attack timing")
                    print("5. Back to main menu{Style.RESET_ALL}")
                    input(f"\n{Fore.GREEN}[?] Press Enter to continue...{Style.RESET_ALL}")
                    continue
                elif menu_choice == "6":
                    configure_network()
                    continue
                elif menu_choice == "7":
                    security_analysis()
                    continue
                elif menu_choice == "8":
                    custom_wordlist = configure_wordlist()
                    if custom_wordlist:
                        print(f"{Fore.GREEN}[+] Custom wordlist loaded successfully{Style.RESET_ALL}")
                    continue
                else:
                    break
            
            print(f"{Fore.YELLOW}[*] Enter target Instagram username: {Style.RESET_ALL}", end="")
            username = input()
            
            simulate_loading()
            simulate_attack(username, attack_mode, custom_wordlist if 'custom_wordlist' in locals() else None)
            
            print(f"\n{Fore.RED}[!] Operation completed{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[*] Remember: Unauthorized access is prohibited{Style.RESET_ALL}")
            
            input(f"\n{Fore.GREEN}[?] Press Enter to return to main menu...{Style.RESET_ALL}")
        
        elif choice == "2":
            show_api_purchase()
        
        elif choice == "3":
            print(f"\n{Fore.YELLOW}[*] Thank you for using our tool{Style.RESET_ALL}")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operation cancelled by user{Style.RESET_ALL}")
        sys.exit(0)
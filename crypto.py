import base64
import urllib.parse

# ---------------- COLORS ----------------
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ---------------- BANNER ----------------
def banner():
    print(f"""{BOLD}{MAGENTA}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   {CYAN} ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ {MAGENTA} ║
║   {CYAN}██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗{MAGENTA} ║
║   {CYAN}██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║{MAGENTA} ║
║   {CYAN}██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║{MAGENTA} ║
║   {CYAN}╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝{MAGENTA}║
║   {CYAN} ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ {MAGENTA}║
║                                                              ║
║   {YELLOW}⚡ Prypto – Encoder / Decoder Toolkit ⚡{MAGENTA}            ║
║   {GREEN}Created by : {CYAN}Harry_Strapper{MAGENTA}                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{RESET}""")

# ---------------- DECODERS ----------------
def decode_base64(t):
    try: return base64.b64decode(t).decode()
    except: return None

def decode_base32(t):
    try: return base64.b32decode(t).decode()
    except: return None

def decode_hex(t):
    try: return bytes.fromhex(t).decode()
    except: return None

def decode_binary(t):
    try: return ''.join(chr(int(b,2)) for b in t.split())
    except: return None

def decode_ascii(t):
    try: return ''.join(chr(int(x)) for x in t.split())
    except: return None

def decode_url(t): return urllib.parse.unquote(t)
def decode_reverse(t): return t[::-1]

def decode_caesar(t):
    res=[]
    for s in range(1,26):
        o=""
        for c in t:
            if c.isalpha():
                b=ord('a') if c.islower() else ord('A')
                o+=chr((ord(c)-b-s)%26+b)
            else: o+=c
        res.append(o)
    return res

MORSE={
'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
'--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
'--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
'...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
'-.--':'Y','--..':'Z','/':' '
}

def decode_morse(t):
    return ''.join(MORSE.get(x,'') for x in t.split())

# ---------------- ENCODERS ----------------
def encode_base64(t): return base64.b64encode(t.encode()).decode()
def encode_base32(t): return base64.b32encode(t.encode()).decode()
def encode_hex(t): return t.encode().hex()
def encode_binary(t): return ' '.join(format(ord(c),'08b') for c in t)
def encode_ascii(t): return ' '.join(str(ord(c)) for c in t)
def encode_url(t): return urllib.parse.quote(t)
def encode_reverse(t): return t[::-1]

def encode_caesar(t,shift=3):
    r=""
    for c in t:
        if c.isalpha():
            b=ord('a') if c.islower() else ord('A')
            r+=chr((ord(c)-b+shift)%26+b)
        else: r+=c
    return r

def encode_morse(t):
    rev={v:k for k,v in MORSE.items()}
    return ' '.join(rev.get(c.upper(),'') for c in t)

# ---------------- IDENTIFY ----------------
def identify_encoding(t):
    print(f"{CYAN}Possible Encoding Types:{RESET}")
    if all(c in "01 " for c in t): print("• Binary")
    if all(c in "0123456789abcdefABCDEF" for c in t): print("• Hex")
    if len(t)%4==0: print("• Base64")
    if "%" in t: print("• URL Encoding")
    if t==t[::-1]: print("• Reverse")

# ---------------- AUTO DECODE ----------------
def auto_decode(t):
    for _ in range(10):
        for f in [
            decode_base64,decode_base32,decode_hex,
            decode_binary,decode_ascii,decode_url,
            decode_reverse,decode_morse
        ]:
            r=f(t)
            if r and r!=t:
                print(f"{YELLOW}→ {r}{RESET}")
                t=r
                break
        else:
            break
    print(f"{GREEN}Final Output: {t}{RESET}")

# ---------------- MAIN LOOP ----------------
def main():
    while True:
        banner()
        print(f"""{CYAN}
1. Identify Encoding
2. Single Decoder
3. Auto Decoder
4. Encoder (Incode)
0. Exit
{RESET}""")

        ch=input("Choose option: ")

        if ch=="0":
            print(f"{GREEN}Exiting... Happy Hacking 😎{RESET}")
            break

        elif ch=="1":
            identify_encoding(input("Enter text: "))

        elif ch=="2":
            print("""
1. Base64   2. Base32   3. Hex
4. Binary  5. ASCII    6. URL
7. Reverse 8. Caesar   9. Morse
""")
            c=input("Select decoder: ")
            t=input("Enter text: ")
            if c=="1": print(decode_base64(t))
            elif c=="2": print(decode_base32(t))
            elif c=="3": print(decode_hex(t))
            elif c=="4": print(decode_binary(t))
            elif c=="5": print(decode_ascii(t))
            elif c=="6": print(decode_url(t))
            elif c=="7": print(decode_reverse(t))
            elif c=="8":
                for r in decode_caesar(t): print(r)
            elif c=="9": print(decode_morse(t))

        elif ch=="3":
            auto_decode(input("Enter text: "))

        elif ch=="4":
            print("""
1. Base64   2. Base32   3. Hex
4. Binary  5. ASCII    6. URL
7. Reverse 8. Caesar   9. Morse
""")
            c=input("Select encoder: ")
            t=input("Enter plain text: ")
            if c=="1": print(encode_base64(t))
            elif c=="2": print(encode_base32(t))
            elif c=="3": print(encode_hex(t))
            elif c=="4": print(encode_binary(t))
            elif c=="5": print(encode_ascii(t))
            elif c=="6": print(encode_url(t))
            elif c=="7": print(encode_reverse(t))
            elif c=="8": print(encode_caesar(t))
            elif c=="9": print(encode_morse(t))

        input(f"\n{YELLOW}Press Enter to return to Main Menu...{RESET}")

if __name__=="__main__":
    main()

import subprocess


def ajascan(komento): 
    print(f"\nExecuting command: {' '.join(komento)}")
    print("\n-----------------------------\n")

    try:
        tulos = subprocess.run(
            komento,
            capture_output=True,
            text=True
        )

        print(tulos.stdout)

        if tulos.stderr:
            print("Error:", tulos.stderr)

    except FileNotFoundError:
        print("Error: Nmap was not found. Make sure it is installed.")
    except Exception as e:
        print("Error:", e)


def run_scan(scannit):
    while True:
        valinta = input("Select an option: ")

        if valinta == "0":
            return

        if valinta not in scannit:
            print("Invalid selection. Try again.")
            continue

        kohde = input("Target: ")

        komento = ["nmap"] + scannit[valinta] + [kohde]

        ajascan(komento)
        return


def host_discovery():

    print("""
====== Host Discovery ======

[1] ARP Scan (-PR)
[2] ICMP Echo Ping (-PE)
[3] ICMP Timestamp Ping (-PP)
[4] TCP SYN Ping (-PS)
[5] TCP ACK Ping (-PA)
[6] UDP Ping (-PU)

[0] Back
""")

    scannit = {
    "1": ["-sn", "-PR"],
    "2": ["-sn", "-PE"],
    "3": ["-sn", "-PP"],
    "4": ["-sn", "-PS80,443"],
    "5": ["-sn", "-PA80,443"],
    "6": ["-sn", "-PU"]
}

    run_scan(scannit)


def port_scanning():

    print("""
====== Port Scanning ======

[1] TCP SYN Scan (-sS)
[2] TCP Connect Scan (-sT)
[3] TCP ACK Scan (-sA)
[4] TCP FIN Scan (-sF)
[5] TCP Xmas Scan (-sX)
[6] TCP Null Scan (-sN)
[7] UDP Scan (-sU)

[0] Back
""")

    scannit = {
        "1": ["-sS", "-T4", "--top-ports", "1000"],
        "2": ["-sT", "-T4", "--top-ports", "1000"],
        "3": ["-sA", "-T4"],
        "4": ["-sF", "-T4"],
        "5": ["-sX", "-T4"],
        "6": ["-sN", "-T4"],
        "7": ["-sU", "--top-ports", "50"]
    }

    run_scan(scannit)


def enumeration():

    print("""
====== Enumeration ======

[1] Service Version Detection (-sV)
[2] OS Detection (-O)
[3] Aggressive Scan (-A)

[0] Back
""")

    scannit = {
        "1": ["-sV"],
        "2": ["-O"],
        "3": ["-A"]
    }

    run_scan(scannit)


def vulnerability_scanning():

    print("""
====== Vulnerability Scanning ======

[1] Nmap Script Engine (-sC)
[2] NSE Scanning (--script vuln)

[0] Back
""")

    scannit = {
        "1": ["-sC"],
        "2": ["--script", "vuln"]
    }

    run_scan(scannit)


def full_scan():

    print("""
====== Full Scan ====== Note: This scan may take a long time to complete and may generate a lot of network traffic.

[1] Full Scan
    (-sS -sV -O -sC --script vuln -T4 -p-)

[0] Back
""")

    scannit = {
        "1": [
            "-sS",
            "-sV",
            "-O",
            "-sC",
            "--script",
            "vuln",
            "-T4",
            "-p-"
        ]
    }

    run_scan(scannit)


def custom_scan():

    print("""
====== Custom Scan ======

Enter custom Nmap scan.

Type 0 to go back.
""")

    custom_options = input("Custom options: ")

    if custom_options == "0":
        return

    if not custom_options:
        print("No options entered.")
        return

    custom_options = custom_options.split()

    target = input("Target: ")

    komento = ["nmap"] + custom_options + [target]

    ajascan(komento)


def main():

    while True:

        print("""
***********************************************
*                                             *
*        ======  Scan Automator ======        *
*                                             *
***********************************************

[1] Host Discovery
[2] Port Scanning
[3] Enumeration
[4] Vulnerability Scanning
[5] Full Scan
[6] Custom Scan

[0] Exit
""")

        valinta = input("Select an option: ")

        if valinta == "1":
            host_discovery()

        elif valinta == "2":
            port_scanning()

        elif valinta == "3":
            enumeration()

        elif valinta == "4":
            vulnerability_scanning()

        elif valinta == "5":
            full_scan()

        elif valinta == "6":
            custom_scan()

        elif valinta == "0":
            print("Exiting...")
            break

        else:
            print("Invalid selection. Please try again.")


main()

        

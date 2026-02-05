import psutil
import time
import datetime
import os
import csv

log_folder = "logs"

if not os.path.exists(log_folder):
    os.mkdir(log_folder)


def get_connections():
    conns = psutil.net_connections()
    active_list = []

    for c in conns:
        if c.status == "ESTABLISHED":
            try:
                p = psutil.Process(c.pid)
                pname = p.name()
            except:
                pname = "Unknown"

            info = {
                "process": pname,
                "local": c.laddr,
                "remote": c.raddr
            }

            active_list.append(info)

    return active_list


def show_connections(data):
    print("\n===== ACTIVE NETWORK CONNECTIONS =====\n")

    for d in data:
        print("Process :", d["process"])
        print("Local   :", d["local"])
        print("Remote  :", d["remote"])
        print("--------------------------------------")


def save_to_file(data):
    time_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = log_folder + "/netlog_" + time_now + ".txt"

    f = open(file_name, "w")

    f.write("Network Log\n")
    f.write(str(datetime.datetime.now()) + "\n\n")

    for d in data:
        line = d["process"] + " -> " + str(d["remote"]) + "\n"
        f.write(line)

    f.close()

    print("\nLog saved as:", file_name)


def save_csv(data):
    time_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = log_folder + "/netlog_" + time_now + ".csv"

    file = open(file_name, "w", newline="")
    writer = csv.writer(file)

    writer.writerow(["Process", "Local Address", "Remote Address"])

    for d in data:
        writer.writerow([d["process"], d["local"], d["remote"]])

    file.close()

    print("\nCSV file saved as:", file_name)


def filter_process(data):
    name = input("\nEnter process name: ")

    found = False

    for d in data:
        if name.lower() in d["process"].lower():
            print("\nProcess :", d["process"])
            print("Local   :", d["local"])
            print("Remote  :", d["remote"])
            print("----------------------------------")
            found = True

    if not found:
        print("\nNo process found with that name")


def monitor_live():
    print("\nLive monitoring started (Press CTRL + C to stop)\n")

    try:
        while True:
            data = get_connections()
            show_connections(data)
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nStopped monitoring")


def show_menu():
    print("\n===== NETLOG MENU =====")
    print("1. View Active Connections")
    print("2. Save Log to Text File")
    print("3. Export Log to CSV")
    print("4. Search by Process Name")
    print("5. Live Monitor")
    print("6. Exit")


# main loop
while True:
    show_menu()

    ch = input("\nEnter option: ")

    data = get_connections()

    if ch == "1":
        show_connections(data)

    elif ch == "2":
        save_to_file(data)

    elif ch == "3":
        save_csv(data)

    elif ch == "4":
        filter_process(data)

    elif ch == "5":
        monitor_live()

    elif ch == "6":
        print("\nExiting program...")
        break

    else:
        print("\nWrong option, try again")


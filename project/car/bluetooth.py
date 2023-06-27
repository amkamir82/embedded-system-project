import bluetooth
import os

DEST_MAC = "3C:F0:11:11:A3:DB"

def send_notif(notif_path: str):
    os.system(f"bluetooth-sendto --device={DEST_MAC} {notif_path}")
    
send_notif("notif_for_car_in_backward.txt")
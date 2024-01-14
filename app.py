from flask import Flask, render_template
from easysnmp import Session

app = Flask(__name__)

def get_connected_devices(router_ip, community_string='public', version=2):
    session = Session(hostname=router_ip, community=community_string, version=version)

    # Replace the OID with the appropriate OID for connected devices on your router
    # The OID for connected devices may vary depending on your router model
    oid_connected_devices = '.1.3.6.1.2.1.4.20'  # Example OID, replace with your actual OID

    # Query the router for the connected devices using SNMP
    devices = session.walk(oid_connected_devices)

    connected_devices = []
    for device in devices:
        # Extract relevant information from the SNMP data
        device_ip = device.oid_index
        device_mac = ':'.join(f'{x:02x}' for x in device.value)

        # Append the device information to the connected_devices list
        connected_devices.append({'ip': device_ip, 'mac': device_mac})

    return connected_devices

@app.route('/')
def index():
    router_ip_address = '192.168.1.2'  # Replace with your router's IP address
    devices = get_connected_devices(router_ip_address)
    return render_template('index.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)

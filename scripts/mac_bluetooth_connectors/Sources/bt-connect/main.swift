import IOBluetooth
import SimpleCLI

//  NOTE: print all device
private func printHelp() {
    print(cliParser.helpString(CommandLine.arguments))
    print("\nGet MAC address of your deivce from the list below.")
    IOBluetoothDevice.pairedDevices().forEach({(device) in
        guard let device = device as? IOBluetoothDevice,
        let addressString = device.addressString,
        let deviceName = device.name
        else { return }
        print("\(addressString) - \(deviceName)")
    })
}

// NOTE: isplay notification on screen
private func displayNotification(_ content: String) {
    if !content.isEmpty {
        Process.launchedProcess(launchPath: "/usr/bin/osascript", arguments: ["-e", "display notification \"\(content)\" with title \"BT connect\""])
    }
}

// NOTE: turn on bluetooth if not open.
private func turnOnBluetoothIfNeeded() {
    guard let bluetoothHost = IOBluetoothHostController.default(),
    bluetoothHost.powerState != kBluetoothHCIPowerStateON else { return }

    if let iobluetoothClass = NSClassFromString("IOBluetoothPreferences") as? NSObject.Type {
        let obj = iobluetoothClass.init()
        let selector = NSSelectorFromString("setPoweredOn:")
        if (obj.responds(to: selector)) {
            obj.perform(selector, with: 1)
        }
    }

    var timeWaited: UInt32 = 0
    let interval: UInt32 = 200000
    while (bluetoothHost.powerState != kBluetoothHCIPowerStateON) {
        usleep(interval)
        timeWaited += interval
        if (timeWaited > 5000000) {
            displayNotification("Failed to turn on Bluetooth")
            exit(-2)
        }
    }
}

// NOTE: init CLI option
let cliParser = SimpleCLI(configuration: [
    Argument(longName: "connect", shortName: "c", type: .keyOnly, defaultValue: "false"),
    Argument(longName: "disconnect", shortName: "d", type: .keyOnly, defaultValue: "false"),
    Argument(longName: "status", shortName: "s", type: .keyOnly, defaultValue: "false"),
    Argument(longName: "address", type: .valueOnly, obligatory: true, inputName: "00-00-00-00-00-00"),
    ])
let dictionary = cliParser.parseArgs(CommandLine.arguments)

guard let deviceAddress = dictionary["address"] else {
    printHelp()
    exit(0)
}

guard let bluetoothDevice = IOBluetoothDevice(addressString: deviceAddress) else {
    displayNotification("Device not found")
    exit(-2)
}

let alreadyConnected = bluetoothDevice.isConnected()
let deviceName = bluetoothDevice.name ?? ""

if !bluetoothDevice.isPaired() {
    displayNotification("Not paired to device")
    exit(-4)
}

var connectOnly = false
if let connectString = dictionary["connect"] {
    connectOnly = Bool(connectString) ?? false
}

var disconnectOnly = false
if let disconnectString = dictionary["disconnect"] {
    disconnectOnly = Bool(disconnectString) ?? false
}

var statusOnly = false
if let statusString = dictionary["status"] {
    statusOnly = Bool(statusString) ?? false
}

if statusOnly {
    displayNotification(alreadyConnected ? "\(deviceName) Connected" : "\(deviceName) Disconnected")
    exit(0)
}

var error : IOReturn = -1

enum ActionType {
    case Connection
    case Disconnect
}

var action : ActionType

let shouldConnect = connectOnly || (!connectOnly && !disconnectOnly && !alreadyConnected)

switch shouldConnect {
  case true:
    action = .Connection    
    turnOnBluetoothIfNeeded()
    error = bluetoothDevice.openConnection()
  case false:
    action = .Disconnect
    error = bluetoothDevice.closeConnection()
}

if error > 0 {
    displayNotification("Error: \(action) failed")
    exit(-1)
} else {
    if action == .Connection && alreadyConnected {
        displayNotification("\(deviceName) already connected")
    } else if action == .Disconnect && !alreadyConnected {
        displayNotification("\(deviceName) already disconnected")
    } else {
        displayNotification( action == .Connection ? "Device '\(deviceName)' successfully disconnected" : "Device '\(deviceName)' successfully disconnected") 
    }
}
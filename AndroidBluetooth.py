"""
Implemented according to AndroidDevelopers
https://developer.android.com/reference/android/bluetooth/BluetoothServerSocket

"""

from jnius import autoclass


BluetoothServerSocket = autoclass('	android.bluetooth.BluetoothServerSocket')

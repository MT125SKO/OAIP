from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self.is_on = False
        self.volume = 0

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass

class Television(Device):
    def turn_on(self):
        self.is_on = True
        print("Телевизор включен")

    def turn_off(self):
        self.is_on = False
        print("Телевизор выключен")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Громкость телевизора установлена на {volume}")

class Radio(Device):
    def turn_on(self):
        self.is_on = True
        print("Радио включено")

    def turn_off(self):
        self.is_on = False
        print("Радио выключено")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Громкость радио установлена на {volume}")

class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def toggle_power(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class IRRemoteControl(RemoteControl):
    def toggle_power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

    def volume_up(self):
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 1)

class BluetoothRemoteControl(RemoteControl):
    def toggle_power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

    def volume_up(self):
        self.device.set_volume(self.device.volume + 5)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 5)

# Мост
class RemoteControlPlatform:
    def __init__(self, remote_control: RemoteControl):
        self._remote_control = remote_control

    def set_remote_control(self, remote_control: RemoteControl):
        self._remote_control = remote_control

    def execute_command(self, command):
        if command == "toggle_power":
            self._remote_control.toggle_power()
        elif command == "volume_up":
            self._remote_control.volume_up()
        elif command == "volume_down":
            self._remote_control.volume_down()
        else:
            print("Неизвестная команда.")

class TVPlatform(RemoteControlPlatform):
    def execute_command(self, command):
        print("TV Platform:")
        super().execute_command(command)

class RadioPlatform(RemoteControlPlatform):
    def execute_command(self, command):
        print("Radio Platform:")
        super().execute_command(command)

# Демонстрация
if __name__ == '__main__':
    tv = Television()
    radio = Radio()

    ir_remote = IRRemoteControl(tv)
    bluetooth_remote = BluetoothRemoteControl(radio)

    tv_platform = TVPlatform(ir_remote)
    radio_platform = RadioPlatform(bluetooth_remote)

    print("Управление телевизором:")
    tv_platform.execute_command("toggle_power")
    tv_platform.execute_command("volume_up")
    tv_platform.execute_command("volume_down")
    tv_platform.execute_command("toggle_power")

    print("\nУправление радио:")
    radio_platform.execute_command("toggle_power")
    radio_platform.execute_command("volume_up")
    radio_platform.execute_command("volume_down")
    radio_platform.execute_command("toggle_power")
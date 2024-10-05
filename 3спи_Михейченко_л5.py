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
        print("Телевизор вкл")

    def turn_off(self):
        self.is_on = False
        print("Телевизор вык")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Громкость на {volume}")

class Radio(Device):
    def turn_on(self):
        self.is_on = True
        print("Радио вкл")

    def turn_off(self):
        self.is_on = False
        print("Радио вык")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Громкость  на {volume}")

class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        self.device.turn_on() if not self.device.is_on else self.device.turn_off()

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class Activ_cont(RemoteControl):
    def volume_up(self):
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 1)

class Pult_control(RemoteControl):
    def volume_up(self):
        self.device.set_volume(self.device.volume + 5)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 5)


class RemoteControlPlatform:
    def __init__(self, remote_control: RemoteControl):
        self._remote_control = remote_control

    def execute_command(self, command):
        if command == "toggle_power":
            self._remote_control.toggle_power()
        elif command == "volume_up":
            self._remote_control.volume_up()
        elif command == "volume_down":
            self._remote_control.volume_down()
        else:
            print("Ошибка")

class TV_box(RemoteControlPlatform):
    def run(self, command):
        print("TV ЯЩИК")
        super().execute_command(command)

class Radio_box(RemoteControlPlatform):
    def execute_command(self, command):
        print("Радио")
        super().execute_command(command)


if __name__ == '__main__':
    tv = Television()
    radio = Radio()

    ir_remote = Activ_cont(tv)
    controller = Pult_control(radio)

    tv_platform = TV_box(ir_remote)
    radio_platform = Radio_box(controller)

    while True:
        print("\nВыберите устройство")
        print("1  Телевизор")
        print("2  Радио")
        print("3  Выход")

        mode = input("Введите номер: ")

        if mode == "1":
            print("\nУправление телевизором")
            while True:
                print("\nВыберите команду:")
                print("1. Вкл/Вык")
                print("2. + громкость")
                print("3. - громкость")
                print("4. Назад")

                num = input("Введите номер: ")
                if num == "1":
                    tv_platform.run("toggle_power")
                elif num == "2":
                    tv_platform.run("volume_up")
                elif num == "3":
                    tv_platform.run("volume_down")
                elif num == "4":
                    break
                else:
                    print("Ошибка")
        elif mode == "2":
            print("\nУправление радио")
            while True:
                print("\nВыберите команду:")
                print("1. Вкл/Вык")
                print("2. + громкость")
                print("3. - громкость")
                print("4. Назад")

                num = input("Введите номер: ")
                if num == "1":
                    radio_platform.execute_command("toggle_power")
                elif num == "2":
                    radio_platform.execute_command("volume_up")
                elif num == "3":
                    radio_platform.execute_command("volume_down")
                elif num == "4":
                    break
                else:
                    print("Ошибка")
        elif mode == "3":
            break
        else:
            print("Ошибка")
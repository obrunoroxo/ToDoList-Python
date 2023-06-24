import os


def verify_system_operational():
    return os.name


def print_path():
    return os.getcwd()


def print_help(operational_system_used: str):
    if operational_system_used == 'posix':
        print("Operating system in use: Unix or Linux")

    elif operational_system_used == 'nt':
        print("Operating system in use: Windows")

    else:
        print("Operating system not supported or identified!")


if __name__ == '__main__':
    system = verify_system_operational()
    print_help(system)
    print_path()
    # print(system, type(system))
config_base = {
    "host": "localhost",
    "port": 3306,
    "debug": False
}

config_desarrollo = {
    "debug": True,
    "log_level": "verbose"
}

config_produccion = {
    "host": "192.168.1.10",
    "log_level": "error"
}

config_final_desarrollo = {**config_base, **config_desarrollo}

config_final_produccion = {**config_base, **config_produccion}

print("Config desarrollo:")
print(config_final_desarrollo)

print("\nConfig producción:")
print(config_final_produccion)


def conectar(host, port, debug, log_level="info"):
    print("\nConectando...")
    print("Host:", host)
    print("Port:", port)
    print("Debug:", debug)
    print("Log level:", log_level)

conectar(**config_final_desarrollo)
conectar(**config_final_produccion)


def conectar2(**kwargs):
    print("\nConectando con kwargs...")
    print(kwargs)

conectar2(**config_final_desarrollo)
conectar2(**config_final_produccion)

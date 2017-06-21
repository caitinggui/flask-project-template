# coding: utf-8

db_config = {
    "mongodb": {
        "mydb": {
            "HOST": "192.168.0.219",
            "PORT": 49010,
            "DB": "db",
            "USER": "mongodb",
            "PASSWORD": "password",
            "MINPOOLSIZE": 200,
            "MAXPOOLSIZE": 300
        }
    },
    "mysql": {
        "server_1": {
            "HOST": "192.168.0.229",
            "PORT": 3306,
            "USER": "mysql",
            "PASSWORD": "password",
            "DB": "db",
            "ID_VALUE": 20000000,
            "POOL_SIZE": 30
        },
        "server_2": {
            "HOST": "192.168.0.220",
            "PORT": 3306,
            "USER": "mysql",
            "PASSWORD": "password",
            "DB": "db",
            "ID_VALUE": 10000000,
            "POOL_SIZE": 30
        }
    },
    "redis": {
        "mydb": {
            "HOST": "192.168.0.219",
            "PORT": 6379,
            "DB": 0,
            "MAX_CONNECTIONS": 200,
            "PASSWORD": "password"
        }
    }
}

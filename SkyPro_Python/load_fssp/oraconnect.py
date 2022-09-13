from dataclasses import dataclass


@dataclass
class OraConnect:
    login: str
    pwd: str
    dsn_tns: str

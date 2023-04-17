from typing import List


class IpAddr:

    def __init__(self, addr: List[str] = [0, 0, 0, 0]) -> None:
        self.addr = addr

    @staticmethod
    def binary_format(addr: str):
        """Construct IP address from binary format.

        >>> IpAddr.binary_format('11001010000010010101111110111100').__str__()
        202.9.95.188
        """
        return IpAddr([int(addr[i*8: i*9], base=2) for i in range(4)])

    def __str__(self) -> str:
        return '.'.join([str(x) for x in self.addr])

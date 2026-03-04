from dataclasses import dataclass


@dataclass
class Order:
    id: int
    track: int
    createdAt: str
    color: list = None
    courierId: int = None
    firstName: str = None
    lastName: str = None
    address: str = None
    metroStation: str = None
    phone: str = None
    rentTime: str = None
    deliveryDate: str = None
    comment: str = None
    updatedAt: str = None
    status: str = None


@dataclass
class Page:
    page: int
    total: int
    limit: int


@dataclass
class Station:
    name: str
    number: int
    color: str


@dataclass
class Orders:
    orders: list[dict] | list[Order]
    pageInfo: dict | Page
    availableStations: list[dict] | list[Station]

    def __post_init__(self):
        self.pageInfo = Page(**self.pageInfo)
        self.orders = [Order(**order) for order in self.orders]
        self.availableStations = [Station(**station) for station in self.availableStations]


@dataclass
class OneOrder:
    order: list[dict] | list[Order]


@dataclass
class NewOrder:
    track: int

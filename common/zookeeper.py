import json
import os
import random
import socket
from uuid import uuid4

from attrs import define
from kazoo.client import KazooClient
from kazoo.protocol.states import KazooState


@define(frozen=True)
class Service:
    host: str
    port: int


_zk: KazooClient | None = None


def init_zookeeper_and_register():
    _init_zookeeper()
    _register_service()


def get_service_from_zookeeper(service: str) -> Service | None:
    global _zk
    assert _zk

    path = f"/providers/{service}"
    children = _zk.get_children(path)

    if not children:
        return None

    idx = random.randint(0, len(children) - 1)

    child = children[idx]
    config, _ = _zk.get(f"/providers/{service}/{child}")
    config = config.decode("utf-8")
    config = json.loads(config)

    return Service(**config)


def _init_zookeeper():
    global _zk

    if not _zk:
        _zk = KazooClient(hosts='127.0.0.1:2181')
        _zk.start(timeout=5)
        _zk.add_listener(_state_change_listener)


def _register_service():
    global _zk

    service = os.environ.get("SERVICE")
    host = socket.getfqdn()
    port = os.environ.get("PORT")

    assert service
    assert host
    assert port

    identifier = str(uuid4())
    path = f"/providers/{service}/{identifier}"
    data = {"host": host, "port": int(port)}
    data_bytes = json.dumps(data).encode("utf-8")

    _zk.create(path, data_bytes, ephemeral=True, makepath=True)


def _state_change_listener(state):
    if state == KazooState.CONNECTED:
        _register_service()

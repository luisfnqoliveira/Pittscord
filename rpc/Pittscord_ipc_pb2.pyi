from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JSONRequest(_message.Message):
    __slots__ = ("admin_name",)
    ADMIN_NAME_FIELD_NUMBER: _ClassVar[int]
    admin_name: str
    def __init__(self, admin_name: _Optional[str] = ...) -> None: ...

class JSONResponse(_message.Message):
    __slots__ = ("json",)
    JSON_FIELD_NUMBER: _ClassVar[int]
    json: str
    def __init__(self, json: _Optional[str] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class ConfigRequest(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: str
    def __init__(self, config: _Optional[str] = ...) -> None: ...

class ConfigResponse(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: int
    def __init__(self, code: _Optional[int] = ...) -> None: ...

class CleanupRequest(_message.Message):
    __slots__ = ("admin_name",)
    ADMIN_NAME_FIELD_NUMBER: _ClassVar[int]
    admin_name: str
    def __init__(self, admin_name: _Optional[str] = ...) -> None: ...

class CleanupResponse(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: int
    def __init__(self, code: _Optional[int] = ...) -> None: ...

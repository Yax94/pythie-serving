"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class StaticStoragePathSourceConfig(google.protobuf.message.Message):
    """Config proto for StaticStoragePathSource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVABLE_NAME_FIELD_NUMBER: builtins.int
    VERSION_NUM_FIELD_NUMBER: builtins.int
    VERSION_PATH_FIELD_NUMBER: builtins.int
    servable_name: typing.Text
    """The single servable name, version number and path to supply statically."""

    version_num: builtins.int
    version_path: typing.Text
    def __init__(self,
        *,
        servable_name: typing.Text = ...,
        version_num: builtins.int = ...,
        version_path: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["servable_name",b"servable_name","version_num",b"version_num","version_path",b"version_path"]) -> None: ...
global___StaticStoragePathSourceConfig = StaticStoragePathSourceConfig

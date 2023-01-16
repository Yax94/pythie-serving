"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RecvBufRespExtra(google.protobuf.message.Message):
    """Extra data needed on a non-RDMA RecvBufResponse."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_CONTENT_FIELD_NUMBER: builtins.int
    @property
    def tensor_content(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(
        self,
        *,
        tensor_content: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tensor_content", b"tensor_content"]) -> None: ...

global___RecvBufRespExtra = RecvBufRespExtra

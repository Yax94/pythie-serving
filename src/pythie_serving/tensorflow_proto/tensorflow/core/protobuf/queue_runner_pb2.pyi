"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.protobuf.error_codes_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueueRunnerDef(google.protobuf.message.Message):
    """Protocol buffer representing a QueueRunner."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QUEUE_NAME_FIELD_NUMBER: builtins.int
    ENQUEUE_OP_NAME_FIELD_NUMBER: builtins.int
    CLOSE_OP_NAME_FIELD_NUMBER: builtins.int
    CANCEL_OP_NAME_FIELD_NUMBER: builtins.int
    QUEUE_CLOSED_EXCEPTION_TYPES_FIELD_NUMBER: builtins.int
    queue_name: typing.Text
    """Queue name."""

    @property
    def enqueue_op_name(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A list of enqueue operations."""
        pass
    close_op_name: typing.Text
    """The operation to run to close the queue."""

    cancel_op_name: typing.Text
    """The operation to run to cancel the queue."""

    @property
    def queue_closed_exception_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[tensorflow.core.protobuf.error_codes_pb2.Code.ValueType]:
        """A list of exception types considered to signal a safely closed queue
        if raised during enqueue operations.
        """
        pass
    def __init__(self,
        *,
        queue_name: typing.Text = ...,
        enqueue_op_name: typing.Optional[typing.Iterable[typing.Text]] = ...,
        close_op_name: typing.Text = ...,
        cancel_op_name: typing.Text = ...,
        queue_closed_exception_types: typing.Optional[typing.Iterable[tensorflow.core.protobuf.error_codes_pb2.Code.ValueType]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cancel_op_name",b"cancel_op_name","close_op_name",b"close_op_name","enqueue_op_name",b"enqueue_op_name","queue_closed_exception_types",b"queue_closed_exception_types","queue_name",b"queue_name"]) -> None: ...
global___QueueRunnerDef = QueueRunnerDef

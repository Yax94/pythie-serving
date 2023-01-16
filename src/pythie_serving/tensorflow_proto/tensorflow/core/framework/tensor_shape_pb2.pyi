"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol buffer representing the shape of tensors."""
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
class TensorShapeProto(google.protobuf.message.Message):
    """Dimensions of a tensor."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Dim(google.protobuf.message.Message):
        """One dimension of the tensor."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SIZE_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        size: builtins.int
        """Size of the tensor in that dimension.
        This value must be >= -1, but values of -1 are reserved for "unknown"
        shapes (values of -1 mean "unknown" dimension).  Certain wrappers
        that work with TensorShapeProto may fail at runtime when deserializing
        a TensorShapeProto containing a dim value of -1.
        """
        name: builtins.str
        """Optional name of the tensor dimension."""
        def __init__(
            self,
            *,
            size: builtins.int = ...,
            name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "size", b"size"]) -> None: ...

    DIM_FIELD_NUMBER: builtins.int
    UNKNOWN_RANK_FIELD_NUMBER: builtins.int
    @property
    def dim(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorShapeProto.Dim]:
        """Dimensions of the tensor, such as {"input", 30}, {"output", 40}
        for a 30 x 40 2D tensor.  If an entry has size -1, this
        corresponds to a dimension of unknown size. The names are
        optional.

        The order of entries in "dim" matters: It indicates the layout of the
        values in the tensor in-memory representation.

        The first entry in "dim" is the outermost dimension used to layout the
        values, the last entry is the innermost dimension.  This matches the
        in-memory layout of RowMajor Eigen tensors.

        If "dim.size()" > 0, "unknown_rank" must be false.
        """
    unknown_rank: builtins.bool
    """If true, the number of dimensions in the shape is unknown.

    If true, "dim.size()" must be 0.
    """
    def __init__(
        self,
        *,
        dim: collections.abc.Iterable[global___TensorShapeProto.Dim] | None = ...,
        unknown_rank: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dim", b"dim", "unknown_rank", b"unknown_rank"]) -> None: ...

global___TensorShapeProto = TensorShapeProto

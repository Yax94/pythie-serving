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
class Profile(google.protobuf.message.Message):
    """Profile is the top-level data that summarizes a program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BY_CATEGORY_FIELD_NUMBER: builtins.int
    BY_PROGRAM_FIELD_NUMBER: builtins.int
    DEVICE_TYPE_FIELD_NUMBER: builtins.int
    BY_CATEGORY_EXCLUDE_IDLE_FIELD_NUMBER: builtins.int
    BY_PROGRAM_EXCLUDE_IDLE_FIELD_NUMBER: builtins.int
    @property
    def by_category(self) -> global___Node:
        """Root of a profile broken down by instruction category."""
    @property
    def by_program(self) -> global___Node:
        """Root of a profile broken down by program."""
    device_type: builtins.str
    """Device type."""
    @property
    def by_category_exclude_idle(self) -> global___Node:
        """Exclude idle ops."""
    @property
    def by_program_exclude_idle(self) -> global___Node: ...
    def __init__(
        self,
        *,
        by_category: global___Node | None = ...,
        by_program: global___Node | None = ...,
        device_type: builtins.str = ...,
        by_category_exclude_idle: global___Node | None = ...,
        by_program_exclude_idle: global___Node | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["by_category", b"by_category", "by_category_exclude_idle", b"by_category_exclude_idle", "by_program", b"by_program", "by_program_exclude_idle", b"by_program_exclude_idle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["by_category", b"by_category", "by_category_exclude_idle", b"by_category_exclude_idle", "by_program", b"by_program", "by_program_exclude_idle", b"by_program_exclude_idle", "device_type", b"device_type"]) -> None: ...

global___Profile = Profile

@typing_extensions.final
class Node(google.protobuf.message.Message):
    """An entry in the profile tree. (An instruction, or set of instructions)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class InstructionCategory(google.protobuf.message.Message):
        """A category of XLA instructions.
        name is a descriptive string, like "data formatting".
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    @typing_extensions.final
    class XLAInstruction(google.protobuf.message.Message):
        """A single XLA instruction.
        name is the unique instruction id, like "%multiply.5".
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class LayoutAnalysis(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            @typing_extensions.final
            class Dimension(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                SIZE_FIELD_NUMBER: builtins.int
                ALIGNMENT_FIELD_NUMBER: builtins.int
                SEMANTICS_FIELD_NUMBER: builtins.int
                size: builtins.int
                """Size of the data in this dimension."""
                alignment: builtins.int
                """Data must be padded to a multiple of alignment."""
                semantics: builtins.str
                """What the dimension represents, e.g. "spatial"."""
                def __init__(
                    self,
                    *,
                    size: builtins.int = ...,
                    alignment: builtins.int = ...,
                    semantics: builtins.str = ...,
                ) -> None: ...
                def ClearField(self, field_name: typing_extensions.Literal["alignment", b"alignment", "semantics", b"semantics", "size", b"size"]) -> None: ...

            DIMENSIONS_FIELD_NUMBER: builtins.int
            @property
            def dimensions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Node.XLAInstruction.LayoutAnalysis.Dimension]:
                """The physical data layout, from most-minor to most-major dimensions."""
            def __init__(
                self,
                *,
                dimensions: collections.abc.Iterable[global___Node.XLAInstruction.LayoutAnalysis.Dimension] | None = ...,
            ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["dimensions", b"dimensions"]) -> None: ...

        OP_FIELD_NUMBER: builtins.int
        EXPRESSION_FIELD_NUMBER: builtins.int
        PROVENANCE_FIELD_NUMBER: builtins.int
        CATEGORY_FIELD_NUMBER: builtins.int
        LAYOUT_FIELD_NUMBER: builtins.int
        COMPUTATION_PRIMITIVE_SIZE_FIELD_NUMBER: builtins.int
        op: builtins.str
        """Opcode like %multiply"""
        expression: builtins.str
        """%multiply = [shape]multiply(operand1, operand2)"""
        provenance: builtins.str
        """Typically the TensorFlow operation name."""
        category: builtins.str
        @property
        def layout(self) -> global___Node.XLAInstruction.LayoutAnalysis:
            """Describes the physical memory layout of the instruction's primary input.
            e.g. for a convolution, this analyzes the image and ignores the kernel.
            """
        computation_primitive_size: builtins.int
        def __init__(
            self,
            *,
            op: builtins.str = ...,
            expression: builtins.str = ...,
            provenance: builtins.str = ...,
            category: builtins.str = ...,
            layout: global___Node.XLAInstruction.LayoutAnalysis | None = ...,
            computation_primitive_size: builtins.int = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["layout", b"layout"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["category", b"category", "computation_primitive_size", b"computation_primitive_size", "expression", b"expression", "layout", b"layout", "op", b"op", "provenance", b"provenance"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    METRICS_FIELD_NUMBER: builtins.int
    CHILDREN_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    XLA_FIELD_NUMBER: builtins.int
    NUM_CHILDREN_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Semantics depend on contents."""
    @property
    def metrics(self) -> global___Metrics:
        """May be omitted e.g. for fused instructions."""
    @property
    def children(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Node]:
        """Subjected to pruning."""
    @property
    def category(self) -> global___Node.InstructionCategory: ...
    @property
    def xla(self) -> global___Node.XLAInstruction: ...
    num_children: builtins.int
    """Total number of children before pruning."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        metrics: global___Metrics | None = ...,
        children: collections.abc.Iterable[global___Node] | None = ...,
        category: global___Node.InstructionCategory | None = ...,
        xla: global___Node.XLAInstruction | None = ...,
        num_children: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["category", b"category", "contents", b"contents", "metrics", b"metrics", "xla", b"xla"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["category", b"category", "children", b"children", "contents", b"contents", "metrics", b"metrics", "name", b"name", "num_children", b"num_children", "xla", b"xla"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["contents", b"contents"]) -> typing_extensions.Literal["category", "xla"] | None: ...

global___Node = Node

@typing_extensions.final
class Metrics(google.protobuf.message.Message):
    """Measurements of an operation (or aggregated set of operations).
    Metrics are always "total" rather than "self".
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_FIELD_NUMBER: builtins.int
    FLOPS_FIELD_NUMBER: builtins.int
    MEMORY_BANDWIDTH_FIELD_NUMBER: builtins.int
    RAW_TIME_FIELD_NUMBER: builtins.int
    RAW_FLOPS_FIELD_NUMBER: builtins.int
    RAW_BYTES_ACCESSED_FIELD_NUMBER: builtins.int
    time: builtins.float
    """Core-time taken by this operation, as a fraction of all operations."""
    flops: builtins.float
    """Floating point computations performed by this operation, as a fraction of
    peak core FLOPS * program time. This representation has useful properties:
     - it is proportional to the number of floating point operations performed
     - utilization is flops/time
     - wasted potential flops is proportional to time - flops
     - it does not reveal the peak core FLOPS of the hardware
    """
    memory_bandwidth: builtins.float
    """The memory bandwidth used to load operands, as a fraction of
    thereotical memory bandwidth on the specific hardware.
    """
    raw_time: builtins.float
    """Elapsed core-time in picoseconds."""
    raw_flops: builtins.float
    """Total floating-point operations performed."""
    raw_bytes_accessed: builtins.float
    """Total bytes accessed (include read/write)."""
    def __init__(
        self,
        *,
        time: builtins.float = ...,
        flops: builtins.float = ...,
        memory_bandwidth: builtins.float = ...,
        raw_time: builtins.float = ...,
        raw_flops: builtins.float = ...,
        raw_bytes_accessed: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["flops", b"flops", "memory_bandwidth", b"memory_bandwidth", "raw_bytes_accessed", b"raw_bytes_accessed", "raw_flops", b"raw_flops", "raw_time", b"raw_time", "time", b"time"]) -> None: ...

global___Metrics = Metrics

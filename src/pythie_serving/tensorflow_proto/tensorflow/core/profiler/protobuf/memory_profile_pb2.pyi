"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _MemoryActivity:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _MemoryActivityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MemoryActivity.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_ACTIVITY: _MemoryActivity.ValueType  # 0
    ALLOCATION: _MemoryActivity.ValueType  # 1
    """Memory allocation in heap."""

    DEALLOCATION: _MemoryActivity.ValueType  # 2
    """Memory deallocation in heap."""

    RESERVATION: _MemoryActivity.ValueType  # 3
    """Memory reservation for stack."""

    EXPANSION: _MemoryActivity.ValueType  # 4
    """Expansion of existing memory allocation."""

class MemoryActivity(_MemoryActivity, metaclass=_MemoryActivityEnumTypeWrapper):
    """The memory activity that causes change of memory state."""
    pass

UNKNOWN_ACTIVITY: MemoryActivity.ValueType  # 0
ALLOCATION: MemoryActivity.ValueType  # 1
"""Memory allocation in heap."""

DEALLOCATION: MemoryActivity.ValueType  # 2
"""Memory deallocation in heap."""

RESERVATION: MemoryActivity.ValueType  # 3
"""Memory reservation for stack."""

EXPANSION: MemoryActivity.ValueType  # 4
"""Expansion of existing memory allocation."""

global___MemoryActivity = MemoryActivity


class MemoryAggregationStats(google.protobuf.message.Message):
    """The aggregated memory stats including heap, stack, free memory and
    fragmentation at a specific time.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STACK_RESERVED_BYTES_FIELD_NUMBER: builtins.int
    HEAP_ALLOCATED_BYTES_FIELD_NUMBER: builtins.int
    FREE_MEMORY_BYTES_FIELD_NUMBER: builtins.int
    FRAGMENTATION_FIELD_NUMBER: builtins.int
    PEAK_BYTES_IN_USE_FIELD_NUMBER: builtins.int
    stack_reserved_bytes: builtins.int
    """Memory usage by stack reservation, in bytes."""

    heap_allocated_bytes: builtins.int
    """Memory usage by heap allocation, in bytes."""

    free_memory_bytes: builtins.int
    """Free memory available for allocation or reservation, in bytes."""

    fragmentation: builtins.float
    """Fragmentation value within [0, 1]."""

    peak_bytes_in_use: builtins.int
    """The peak memory usage over the entire program (lifetime of memory
    allocator). It monotonically increases with upper limit as memory capacity.
    """

    def __init__(self,
        *,
        stack_reserved_bytes: builtins.int = ...,
        heap_allocated_bytes: builtins.int = ...,
        free_memory_bytes: builtins.int = ...,
        fragmentation: builtins.float = ...,
        peak_bytes_in_use: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fragmentation",b"fragmentation","free_memory_bytes",b"free_memory_bytes","heap_allocated_bytes",b"heap_allocated_bytes","peak_bytes_in_use",b"peak_bytes_in_use","stack_reserved_bytes",b"stack_reserved_bytes"]) -> None: ...
global___MemoryAggregationStats = MemoryAggregationStats

class MemoryActivityMetadata(google.protobuf.message.Message):
    """The metadata associated with each memory allocation/deallocation. It can
    also be interpreted as the metadata for the delta of memory state.
    Next ID: 10
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MEMORY_ACTIVITY_FIELD_NUMBER: builtins.int
    REQUESTED_BYTES_FIELD_NUMBER: builtins.int
    ALLOCATION_BYTES_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    TF_OP_NAME_FIELD_NUMBER: builtins.int
    STEP_ID_FIELD_NUMBER: builtins.int
    REGION_TYPE_FIELD_NUMBER: builtins.int
    DATA_TYPE_FIELD_NUMBER: builtins.int
    TENSOR_SHAPE_FIELD_NUMBER: builtins.int
    memory_activity: global___MemoryActivity.ValueType
    """The activity associated with the MemoryProfileSnapshot."""

    requested_bytes: builtins.int
    """The requested memory size in bytes from the caller of memory allocation.
    Should be a positive number.
    """

    allocation_bytes: builtins.int
    """The allocated (block/chunk) size for the memory allocation.
    Should be a positive number.
    """

    address: builtins.int
    """Starting address of the allocated memory chunk/block."""

    tf_op_name: typing.Text
    """TensorFlow Op name for the memory activity."""

    step_id: builtins.int
    """Step Id at which the memory activity occurred."""

    region_type: typing.Text
    """Tensor memory region type including "output", "temp", "persist", and
    "dynamic".
    """

    data_type: typing.Text
    """From enum DataType defined in tensorflow/core/framework/types.proto."""

    tensor_shape: typing.Text
    """Tensor shape printed in string, e.g. "[3, 3, 512, 512]"."""

    def __init__(self,
        *,
        memory_activity: global___MemoryActivity.ValueType = ...,
        requested_bytes: builtins.int = ...,
        allocation_bytes: builtins.int = ...,
        address: builtins.int = ...,
        tf_op_name: typing.Text = ...,
        step_id: builtins.int = ...,
        region_type: typing.Text = ...,
        data_type: typing.Text = ...,
        tensor_shape: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","allocation_bytes",b"allocation_bytes","data_type",b"data_type","memory_activity",b"memory_activity","region_type",b"region_type","requested_bytes",b"requested_bytes","step_id",b"step_id","tensor_shape",b"tensor_shape","tf_op_name",b"tf_op_name"]) -> None: ...
global___MemoryActivityMetadata = MemoryActivityMetadata

class MemoryProfileSnapshot(google.protobuf.message.Message):
    """Profile snapshot of the TensorFlow memory at runtime, including
    MemoryAggregationStats (memory usage breakdown etc.), and
    MemoryActivityMetadata (allocation or deallocation, TF Op name etc.).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIME_OFFSET_PS_FIELD_NUMBER: builtins.int
    AGGREGATION_STATS_FIELD_NUMBER: builtins.int
    ACTIVITY_METADATA_FIELD_NUMBER: builtins.int
    time_offset_ps: builtins.int
    """Memory activity timestamp."""

    @property
    def aggregation_stats(self) -> global___MemoryAggregationStats:
        """The memory aggregation stats at the snapshot time."""
        pass
    @property
    def activity_metadata(self) -> global___MemoryActivityMetadata:
        """The metadata for the memory activity at the snapshot time."""
        pass
    def __init__(self,
        *,
        time_offset_ps: builtins.int = ...,
        aggregation_stats: typing.Optional[global___MemoryAggregationStats] = ...,
        activity_metadata: typing.Optional[global___MemoryActivityMetadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["activity_metadata",b"activity_metadata","aggregation_stats",b"aggregation_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activity_metadata",b"activity_metadata","aggregation_stats",b"aggregation_stats","time_offset_ps",b"time_offset_ps"]) -> None: ...
global___MemoryProfileSnapshot = MemoryProfileSnapshot

class MemoryProfileSummary(google.protobuf.message.Message):
    """The summary of memory profile within the profiling window duration."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PEAK_BYTES_USAGE_LIFETIME_FIELD_NUMBER: builtins.int
    PEAK_STATS_FIELD_NUMBER: builtins.int
    PEAK_STATS_TIME_PS_FIELD_NUMBER: builtins.int
    MEMORY_CAPACITY_FIELD_NUMBER: builtins.int
    peak_bytes_usage_lifetime: builtins.int
    """The peak memory usage over the entire program (lifetime of memory
    allocator).
    """

    @property
    def peak_stats(self) -> global___MemoryAggregationStats:
        """The peak memory usage stats within the profiling window."""
        pass
    peak_stats_time_ps: builtins.int
    """The timestamp for peak memory usage within the profiling window."""

    memory_capacity: builtins.int
    """The memory capacity of the allocator."""

    def __init__(self,
        *,
        peak_bytes_usage_lifetime: builtins.int = ...,
        peak_stats: typing.Optional[global___MemoryAggregationStats] = ...,
        peak_stats_time_ps: builtins.int = ...,
        memory_capacity: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["peak_stats",b"peak_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["memory_capacity",b"memory_capacity","peak_bytes_usage_lifetime",b"peak_bytes_usage_lifetime","peak_stats",b"peak_stats","peak_stats_time_ps",b"peak_stats_time_ps"]) -> None: ...
global___MemoryProfileSummary = MemoryProfileSummary

class ActiveAllocation(google.protobuf.message.Message):
    """The active memory allocations at the peak memory usage."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SNAPSHOT_INDEX_FIELD_NUMBER: builtins.int
    SPECIAL_INDEX_FIELD_NUMBER: builtins.int
    NUM_OCCURRENCES_FIELD_NUMBER: builtins.int
    snapshot_index: builtins.int
    """The index of a snapshot in the time-sorted list, used to fetch the
    MemoryActivityMetadata at front end from the memory_profile_snapshots list.
    """

    special_index: builtins.int
    """The index of MemoryActivityMetadata in the special_allocations list."""

    num_occurrences: builtins.int
    """Number of occurrences for identical memory allocations."""

    def __init__(self,
        *,
        snapshot_index: builtins.int = ...,
        special_index: builtins.int = ...,
        num_occurrences: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["num_occurrences",b"num_occurrences","snapshot_index",b"snapshot_index","special_index",b"special_index"]) -> None: ...
global___ActiveAllocation = ActiveAllocation

class PerAllocatorMemoryProfile(google.protobuf.message.Message):
    """Memory profile snapshots per memory allocator."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MEMORY_PROFILE_SNAPSHOTS_FIELD_NUMBER: builtins.int
    PROFILE_SUMMARY_FIELD_NUMBER: builtins.int
    ACTIVE_ALLOCATIONS_FIELD_NUMBER: builtins.int
    SPECIAL_ALLOCATIONS_FIELD_NUMBER: builtins.int
    @property
    def memory_profile_snapshots(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MemoryProfileSnapshot]:
        """A list of MemoryProfileSnapshots sorted by time_offset_ps."""
        pass
    @property
    def profile_summary(self) -> global___MemoryProfileSummary:
        """The summary of memory profile (e.g. the peak memory usage)."""
        pass
    @property
    def active_allocations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ActiveAllocation]:
        """The rows in the table of active allocations at peak memory usage within
        profiling window.
        """
        pass
    @property
    def special_allocations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MemoryActivityMetadata]:
        """The special allocations (e.g. pre-allocated heap memory, stack reservation)
        that are not captured in the MemoryActivityMetadata of
        memory_profile_snapshots. Need to handle separately.
        """
        pass
    def __init__(self,
        *,
        memory_profile_snapshots: typing.Optional[typing.Iterable[global___MemoryProfileSnapshot]] = ...,
        profile_summary: typing.Optional[global___MemoryProfileSummary] = ...,
        active_allocations: typing.Optional[typing.Iterable[global___ActiveAllocation]] = ...,
        special_allocations: typing.Optional[typing.Iterable[global___MemoryActivityMetadata]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["profile_summary",b"profile_summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_allocations",b"active_allocations","memory_profile_snapshots",b"memory_profile_snapshots","profile_summary",b"profile_summary","special_allocations",b"special_allocations"]) -> None: ...
global___PerAllocatorMemoryProfile = PerAllocatorMemoryProfile

class MemoryProfile(google.protobuf.message.Message):
    """Data for memory usage analysis in one host."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MemoryProfilePerAllocatorEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___PerAllocatorMemoryProfile: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___PerAllocatorMemoryProfile] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    MEMORY_PROFILE_PER_ALLOCATOR_FIELD_NUMBER: builtins.int
    NUM_HOSTS_FIELD_NUMBER: builtins.int
    MEMORY_IDS_FIELD_NUMBER: builtins.int
    @property
    def memory_profile_per_allocator(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___PerAllocatorMemoryProfile]:
        """A map from memory allocator's id to PerAllocatorMemoryProfile for memory
        usage analysis on this host.
        """
        pass
    num_hosts: builtins.int
    """Number of hosts profiled, used to populate host selection list at front
    end.
    """

    @property
    def memory_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Ids for profiled memory allocators, used to populate memory selection list
        at front end.
        """
        pass
    def __init__(self,
        *,
        memory_profile_per_allocator: typing.Optional[typing.Mapping[typing.Text, global___PerAllocatorMemoryProfile]] = ...,
        num_hosts: builtins.int = ...,
        memory_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["memory_ids",b"memory_ids","memory_profile_per_allocator",b"memory_profile_per_allocator","num_hosts",b"num_hosts"]) -> None: ...
global___MemoryProfile = MemoryProfile

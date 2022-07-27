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

class _MemoryRegion:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _MemoryRegionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MemoryRegion.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HBM: _MemoryRegion.ValueType  # 1
class MemoryRegion(_MemoryRegion, metaclass=_MemoryRegionEnumTypeWrapper):
    pass

HBM: MemoryRegion.ValueType  # 1
global___MemoryRegion = MemoryRegion


class ChipCoordinate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.int
    y: builtins.int
    z: builtins.int
    def __init__(self,
        *,
        x: typing.Optional[builtins.int] = ...,
        y: typing.Optional[builtins.int] = ...,
        z: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["x",b"x","y",b"y","z",b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["x",b"x","y",b"y","z",b"z"]) -> None: ...
global___ChipCoordinate = ChipCoordinate

class TpuCoreInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    CORE_ON_CHIP_INDEX_FIELD_NUMBER: builtins.int
    CORE_ON_HOST_INDEX_FIELD_NUMBER: builtins.int
    HBM_BYTES_AVAILABLE_FIELD_NUMBER: builtins.int
    HBM_BYTES_ALLOCATABLE_FIELD_NUMBER: builtins.int
    id: builtins.int
    core_on_chip_index: builtins.int
    core_on_host_index: builtins.int
    hbm_bytes_available: builtins.int
    hbm_bytes_allocatable: builtins.int
    def __init__(self,
        *,
        id: typing.Optional[builtins.int] = ...,
        core_on_chip_index: typing.Optional[builtins.int] = ...,
        core_on_host_index: typing.Optional[builtins.int] = ...,
        hbm_bytes_available: typing.Optional[builtins.int] = ...,
        hbm_bytes_allocatable: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["core_on_chip_index",b"core_on_chip_index","core_on_host_index",b"core_on_host_index","hbm_bytes_allocatable",b"hbm_bytes_allocatable","hbm_bytes_available",b"hbm_bytes_available","id",b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["core_on_chip_index",b"core_on_chip_index","core_on_host_index",b"core_on_host_index","hbm_bytes_allocatable",b"hbm_bytes_allocatable","hbm_bytes_available",b"hbm_bytes_available","id",b"id"]) -> None: ...
global___TpuCoreInfo = TpuCoreInfo

class TpuChipInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CORE_FIELD_NUMBER: builtins.int
    HOST_ID_FIELD_NUMBER: builtins.int
    CHIP_COORD_FIELD_NUMBER: builtins.int
    @property
    def core(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TpuCoreInfo]: ...
    host_id: builtins.int
    @property
    def chip_coord(self) -> global___ChipCoordinate: ...
    def __init__(self,
        *,
        core: typing.Optional[typing.Iterable[global___TpuCoreInfo]] = ...,
        host_id: typing.Optional[builtins.int] = ...,
        chip_coord: typing.Optional[global___ChipCoordinate] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["chip_coord",b"chip_coord","host_id",b"host_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chip_coord",b"chip_coord","core",b"core","host_id",b"host_id"]) -> None: ...
global___TpuChipInfo = TpuChipInfo

class CpuInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NUM_CPU_CORES_FIELD_NUMBER: builtins.int
    CPU_LOAD_AVERAGE_1MIN_FIELD_NUMBER: builtins.int
    RAM_BYTES_TOTAL_FIELD_NUMBER: builtins.int
    RAM_BYTES_AVAILABLE_FIELD_NUMBER: builtins.int
    num_cpu_cores: builtins.int
    cpu_load_average_1min: builtins.float
    ram_bytes_total: builtins.int
    ram_bytes_available: builtins.int
    def __init__(self,
        *,
        num_cpu_cores: typing.Optional[builtins.int] = ...,
        cpu_load_average_1min: typing.Optional[builtins.float] = ...,
        ram_bytes_total: typing.Optional[builtins.int] = ...,
        ram_bytes_available: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cpu_load_average_1min",b"cpu_load_average_1min","num_cpu_cores",b"num_cpu_cores","ram_bytes_available",b"ram_bytes_available","ram_bytes_total",b"ram_bytes_total"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cpu_load_average_1min",b"cpu_load_average_1min","num_cpu_cores",b"num_cpu_cores","ram_bytes_available",b"ram_bytes_available","ram_bytes_total",b"ram_bytes_total"]) -> None: ...
global___CpuInfo = CpuInfo

class SystemInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TPU_CHIP_FIELD_NUMBER: builtins.int
    CPU_FIELD_NUMBER: builtins.int
    LOCAL_CORE_FIELD_NUMBER: builtins.int
    HOST_ID_FIELD_NUMBER: builtins.int
    HOST_COUNT_FIELD_NUMBER: builtins.int
    CHIP_COUNT_FIELD_NUMBER: builtins.int
    CORE_COUNT_FIELD_NUMBER: builtins.int
    @property
    def tpu_chip(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TpuChipInfo]: ...
    @property
    def cpu(self) -> global___CpuInfo: ...
    @property
    def local_core(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TpuCoreInfo]: ...
    host_id: builtins.int
    host_count: builtins.int
    chip_count: builtins.int
    core_count: builtins.int
    def __init__(self,
        *,
        tpu_chip: typing.Optional[typing.Iterable[global___TpuChipInfo]] = ...,
        cpu: typing.Optional[global___CpuInfo] = ...,
        local_core: typing.Optional[typing.Iterable[global___TpuCoreInfo]] = ...,
        host_id: typing.Optional[builtins.int] = ...,
        host_count: typing.Optional[builtins.int] = ...,
        chip_count: typing.Optional[builtins.int] = ...,
        core_count: typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["chip_count",b"chip_count","core_count",b"core_count","cpu",b"cpu","host_count",b"host_count","host_id",b"host_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["chip_count",b"chip_count","core_count",b"core_count","cpu",b"cpu","host_count",b"host_count","host_id",b"host_id","local_core",b"local_core","tpu_chip",b"tpu_chip"]) -> None: ...
global___SystemInfo = SystemInfo

class TpuDriverConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class GrpcConfig(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CONNECTION_TIMEOUT_SECS_FIELD_NUMBER: builtins.int
        KEEPALIVE_TIMEOUT_SECS_FIELD_NUMBER: builtins.int
        connection_timeout_secs: builtins.int
        """Time in seconds before the initial connection to the server will timeout."""

        keepalive_timeout_secs: builtins.int
        """Time in seconds the server may be unresponsive before terminating the
        connection.
        """

        def __init__(self,
            *,
            connection_timeout_secs: typing.Optional[builtins.int] = ...,
            keepalive_timeout_secs: typing.Optional[builtins.int] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["connection_timeout_secs",b"connection_timeout_secs","keepalive_timeout_secs",b"keepalive_timeout_secs"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["connection_timeout_secs",b"connection_timeout_secs","keepalive_timeout_secs",b"keepalive_timeout_secs"]) -> None: ...

    WORKER_FIELD_NUMBER: builtins.int
    GRPC_FIELD_NUMBER: builtins.int
    worker: typing.Text
    @property
    def grpc(self) -> global___TpuDriverConfig.GrpcConfig: ...
    def __init__(self,
        *,
        worker: typing.Optional[typing.Text] = ...,
        grpc: typing.Optional[global___TpuDriverConfig.GrpcConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["grpc",b"grpc","worker",b"worker"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["grpc",b"grpc","worker",b"worker"]) -> None: ...
global___TpuDriverConfig = TpuDriverConfig

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.compiler.xla.service.hlo_pb2
import tensorflow.compiler.xla.xla_data_pb2
import tensorflow.core.protobuf.autotuning_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ConvInstructionLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INSTRUCTION_FIELD_NUMBER: builtins.int
    OPERAND_SHAPES_FIELD_NUMBER: builtins.int
    RESULT_ADDRESS_FIELD_NUMBER: builtins.int
    OPERAND_ADDRESSES_FIELD_NUMBER: builtins.int
    @property
    def instruction(self) -> tensorflow.compiler.xla.service.hlo_pb2.HloInstructionProto: ...
    @property
    def operand_shapes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.compiler.xla.xla_data_pb2.ShapeProto]: ...
    result_address: builtins.int
    @property
    def operand_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        instruction: typing.Optional[tensorflow.compiler.xla.service.hlo_pb2.HloInstructionProto] = ...,
        operand_shapes: typing.Optional[typing.Iterable[tensorflow.compiler.xla.xla_data_pb2.ShapeProto]] = ...,
        result_address: builtins.int = ...,
        operand_addresses: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["instruction",b"instruction"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["instruction",b"instruction","operand_addresses",b"operand_addresses","operand_shapes",b"operand_shapes","result_address",b"result_address"]) -> None: ...
global___ConvInstructionLog = ConvInstructionLog

class DenylistedAlgorithm(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    TENSOR_OPS_FIELD_NUMBER: builtins.int
    id: builtins.int
    tensor_ops: builtins.bool
    def __init__(self,
        *,
        id: builtins.int = ...,
        tensor_ops: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","tensor_ops",b"tensor_ops"]) -> None: ...
global___DenylistedAlgorithm = DenylistedAlgorithm

class AlgorithmDenylistEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HLO_FIELD_NUMBER: builtins.int
    CC_FIELD_NUMBER: builtins.int
    CUDNN_VERSION_FIELD_NUMBER: builtins.int
    BLAS_VERSION_FIELD_NUMBER: builtins.int
    ALGOS_FIELD_NUMBER: builtins.int
    hlo: typing.Text
    @property
    def cc(self) -> tensorflow.core.protobuf.autotuning_pb2.ComputeCapability: ...
    @property
    def cudnn_version(self) -> tensorflow.core.protobuf.autotuning_pb2.CudnnVersion: ...
    blas_version: typing.Text
    @property
    def algos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DenylistedAlgorithm]: ...
    def __init__(self,
        *,
        hlo: typing.Text = ...,
        cc: typing.Optional[tensorflow.core.protobuf.autotuning_pb2.ComputeCapability] = ...,
        cudnn_version: typing.Optional[tensorflow.core.protobuf.autotuning_pb2.CudnnVersion] = ...,
        blas_version: typing.Text = ...,
        algos: typing.Optional[typing.Iterable[global___DenylistedAlgorithm]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cc",b"cc","cudnn_version",b"cudnn_version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["algos",b"algos","blas_version",b"blas_version","cc",b"cc","cudnn_version",b"cudnn_version","hlo",b"hlo"]) -> None: ...
global___AlgorithmDenylistEntry = AlgorithmDenylistEntry

class AlgorithmDenylist(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTRIES_FIELD_NUMBER: builtins.int
    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AlgorithmDenylistEntry]: ...
    def __init__(self,
        *,
        entries: typing.Optional[typing.Iterable[global___AlgorithmDenylistEntry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entries",b"entries"]) -> None: ...
global___AlgorithmDenylist = AlgorithmDenylist

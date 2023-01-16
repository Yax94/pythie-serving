"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2
import tensorflow.compiler.xla.service.hlo_pb2
import tensorflow.compiler.xla.xla_data_pb2
import tensorflow.compiler.xla.xla_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class StatusMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: builtins.int
    message: builtins.str
    def __init__(
        self,
        *,
        code: builtins.int | None = ...,
        message: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["code", b"code", "message", b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "message", b"message"]) -> None: ...

global___StatusMessage = StatusMessage

@typing_extensions.final
class AllocateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CORE_ID_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    NUM_BYTES_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    core_id: builtins.int
    region: tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2.MemoryRegion.ValueType
    num_bytes: builtins.int
    @property
    def shape(self) -> tensorflow.compiler.xla.xla_data_pb2.ShapeProto: ...
    def __init__(
        self,
        *,
        core_id: builtins.int | None = ...,
        region: tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2.MemoryRegion.ValueType | None = ...,
        num_bytes: builtins.int | None = ...,
        shape: tensorflow.compiler.xla.xla_data_pb2.ShapeProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["core_id", b"core_id", "num_bytes", b"num_bytes", "region", b"region", "shape", b"shape", "size", b"size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["core_id", b"core_id", "num_bytes", b"num_bytes", "region", b"region", "shape", b"shape", "size", b"size"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["size", b"size"]) -> typing_extensions.Literal["num_bytes", "shape"] | None: ...

global___AllocateRequest = AllocateRequest

@typing_extensions.final
class AllocateTupleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CORE_ID_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    CHILDREN_FIELD_NUMBER: builtins.int
    core_id: builtins.int
    region: tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2.MemoryRegion.ValueType
    @property
    def children(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        core_id: builtins.int | None = ...,
        region: tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2.MemoryRegion.ValueType | None = ...,
        children: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["core_id", b"core_id", "region", b"region"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["children", b"children", "core_id", b"core_id", "region", b"region"]) -> None: ...

global___AllocateTupleRequest = AllocateTupleRequest

@typing_extensions.final
class DeallocateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HANDLE_FIELD_NUMBER: builtins.int
    handle: builtins.int
    def __init__(
        self,
        *,
        handle: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handle", b"handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handle", b"handle"]) -> None: ...

global___DeallocateRequest = DeallocateRequest

@typing_extensions.final
class TransferToDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_HANDLE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    target_handle: builtins.int
    data: builtins.bytes
    def __init__(
        self,
        *,
        target_handle: builtins.int | None = ...,
        data: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data", "target_handle", b"target_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "target_handle", b"target_handle"]) -> None: ...

global___TransferToDeviceRequest = TransferToDeviceRequest

@typing_extensions.final
class TransferFromDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_HANDLE_FIELD_NUMBER: builtins.int
    source_handle: builtins.int
    def __init__(
        self,
        *,
        source_handle: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["source_handle", b"source_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["source_handle", b"source_handle"]) -> None: ...

global___TransferFromDeviceRequest = TransferFromDeviceRequest

@typing_extensions.final
class TransferFromDeviceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    def __init__(
        self,
        *,
        data: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___TransferFromDeviceResponse = TransferFromDeviceResponse

@typing_extensions.final
class TransferFromDeviceToDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_HANDLE_FIELD_NUMBER: builtins.int
    TARGET_HANDLE_FIELD_NUMBER: builtins.int
    source_handle: builtins.int
    target_handle: builtins.int
    def __init__(
        self,
        *,
        source_handle: builtins.int | None = ...,
        target_handle: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["source_handle", b"source_handle", "target_handle", b"target_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["source_handle", b"source_handle", "target_handle", b"target_handle"]) -> None: ...

global___TransferFromDeviceToDeviceRequest = TransferFromDeviceToDeviceRequest

@typing_extensions.final
class CompileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HLO_PROGRAM_FIELD_NUMBER: builtins.int
    NUM_REPLICAS_FIELD_NUMBER: builtins.int
    DEBUG_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def hlo_program(self) -> tensorflow.compiler.xla.service.hlo_pb2.HloProto: ...
    num_replicas: builtins.int
    @property
    def debug_options(self) -> tensorflow.compiler.xla.xla_pb2.DebugOptions: ...
    def __init__(
        self,
        *,
        hlo_program: tensorflow.compiler.xla.service.hlo_pb2.HloProto | None = ...,
        num_replicas: builtins.int | None = ...,
        debug_options: tensorflow.compiler.xla.xla_pb2.DebugOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["debug_options", b"debug_options", "hlo_program", b"hlo_program", "num_replicas", b"num_replicas"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["debug_options", b"debug_options", "hlo_program", b"hlo_program", "num_replicas", b"num_replicas"]) -> None: ...

global___CompileRequest = CompileRequest

@typing_extensions.final
class CompiledProgramMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROGRAM_SHAPE_FIELD_NUMBER: builtins.int
    @property
    def program_shape(self) -> tensorflow.compiler.xla.xla_data_pb2.ProgramShapeProto: ...
    def __init__(
        self,
        *,
        program_shape: tensorflow.compiler.xla.xla_data_pb2.ProgramShapeProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["program_shape", b"program_shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["program_shape", b"program_shape"]) -> None: ...

global___CompiledProgramMetadata = CompiledProgramMetadata

@typing_extensions.final
class CompileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___CompiledProgramMetadata: ...
    def __init__(
        self,
        *,
        metadata: global___CompiledProgramMetadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> None: ...

global___CompileResponse = CompileResponse

@typing_extensions.final
class LoadProgramRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CORE_ID_FIELD_NUMBER: builtins.int
    COMPILED_PROGRAM_HANDLE_FIELD_NUMBER: builtins.int
    core_id: builtins.int
    compiled_program_handle: builtins.int
    def __init__(
        self,
        *,
        core_id: builtins.int | None = ...,
        compiled_program_handle: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compiled_program_handle", b"compiled_program_handle", "core_id", b"core_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compiled_program_handle", b"compiled_program_handle", "core_id", b"core_id"]) -> None: ...

global___LoadProgramRequest = LoadProgramRequest

@typing_extensions.final
class UnloadProgramRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOADED_PROGRAM_HANDLE_FIELD_NUMBER: builtins.int
    loaded_program_handle: builtins.int
    def __init__(
        self,
        *,
        loaded_program_handle: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["loaded_program_handle", b"loaded_program_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["loaded_program_handle", b"loaded_program_handle"]) -> None: ...

global___UnloadProgramRequest = UnloadProgramRequest

@typing_extensions.final
class ExecuteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOADED_PROGRAM_HANDLE_FIELD_NUMBER: builtins.int
    INPUT_HANDLE_FIELD_NUMBER: builtins.int
    OUTPUT_HANDLE_FIELD_NUMBER: builtins.int
    DEVICE_ASSIGNMENT_FIELD_NUMBER: builtins.int
    loaded_program_handle: builtins.int
    @property
    def input_handle(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def output_handle(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def device_assignment(self) -> tensorflow.compiler.xla.xla_data_pb2.DeviceAssignmentProto: ...
    def __init__(
        self,
        *,
        loaded_program_handle: builtins.int | None = ...,
        input_handle: collections.abc.Iterable[builtins.int] | None = ...,
        output_handle: collections.abc.Iterable[builtins.int] | None = ...,
        device_assignment: tensorflow.compiler.xla.xla_data_pb2.DeviceAssignmentProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["device_assignment", b"device_assignment", "loaded_program_handle", b"loaded_program_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["device_assignment", b"device_assignment", "input_handle", b"input_handle", "loaded_program_handle", b"loaded_program_handle", "output_handle", b"output_handle"]) -> None: ...

global___ExecuteRequest = ExecuteRequest

@typing_extensions.final
class StreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Entry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ALLOC_FIELD_NUMBER: builtins.int
        ALLOC_TUPLE_FIELD_NUMBER: builtins.int
        DEALLOC_FIELD_NUMBER: builtins.int
        TRANSFER_TO_FIELD_NUMBER: builtins.int
        TRANSFER_FROM_FIELD_NUMBER: builtins.int
        TRANSFER_FROM_TO_FIELD_NUMBER: builtins.int
        COMPILE_FIELD_NUMBER: builtins.int
        LOAD_FIELD_NUMBER: builtins.int
        UNLOAD_FIELD_NUMBER: builtins.int
        EXECUTE_FIELD_NUMBER: builtins.int
        WAIT_FOR_ID_FIELD_NUMBER: builtins.int
        OPERATION_ID_FIELD_NUMBER: builtins.int
        THREAD_ID_FIELD_NUMBER: builtins.int
        @property
        def alloc(self) -> global___AllocateRequest: ...
        @property
        def alloc_tuple(self) -> global___AllocateTupleRequest: ...
        @property
        def dealloc(self) -> global___DeallocateRequest: ...
        @property
        def transfer_to(self) -> global___TransferToDeviceRequest: ...
        @property
        def transfer_from(self) -> global___TransferFromDeviceRequest: ...
        @property
        def transfer_from_to(self) -> global___TransferFromDeviceToDeviceRequest: ...
        @property
        def compile(self) -> global___CompileRequest: ...
        @property
        def load(self) -> global___LoadProgramRequest: ...
        @property
        def unload(self) -> global___UnloadProgramRequest: ...
        @property
        def execute(self) -> global___ExecuteRequest: ...
        @property
        def wait_for_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
            """If specified, a list of encoded EventId values."""
        operation_id: builtins.int
        """A unique, encoded EventId value.
        For Allocate, Compile, and Load, this also defines the result handle.
        """
        thread_id: builtins.int
        """A unique identifier for the thread that issued this request. Currently
        for debugging purposes only.
        """
        def __init__(
            self,
            *,
            alloc: global___AllocateRequest | None = ...,
            alloc_tuple: global___AllocateTupleRequest | None = ...,
            dealloc: global___DeallocateRequest | None = ...,
            transfer_to: global___TransferToDeviceRequest | None = ...,
            transfer_from: global___TransferFromDeviceRequest | None = ...,
            transfer_from_to: global___TransferFromDeviceToDeviceRequest | None = ...,
            compile: global___CompileRequest | None = ...,
            load: global___LoadProgramRequest | None = ...,
            unload: global___UnloadProgramRequest | None = ...,
            execute: global___ExecuteRequest | None = ...,
            wait_for_id: collections.abc.Iterable[builtins.int] | None = ...,
            operation_id: builtins.int | None = ...,
            thread_id: builtins.int | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["alloc", b"alloc", "alloc_tuple", b"alloc_tuple", "compile", b"compile", "dealloc", b"dealloc", "execute", b"execute", "load", b"load", "operation_id", b"operation_id", "request", b"request", "thread_id", b"thread_id", "transfer_from", b"transfer_from", "transfer_from_to", b"transfer_from_to", "transfer_to", b"transfer_to", "unload", b"unload"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["alloc", b"alloc", "alloc_tuple", b"alloc_tuple", "compile", b"compile", "dealloc", b"dealloc", "execute", b"execute", "load", b"load", "operation_id", b"operation_id", "request", b"request", "thread_id", b"thread_id", "transfer_from", b"transfer_from", "transfer_from_to", b"transfer_from_to", "transfer_to", b"transfer_to", "unload", b"unload", "wait_for_id", b"wait_for_id"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["request", b"request"]) -> typing_extensions.Literal["alloc", "alloc_tuple", "dealloc", "transfer_to", "transfer_from", "transfer_from_to", "compile", "load", "unload", "execute"] | None: ...

    ENTRY_FIELD_NUMBER: builtins.int
    @property
    def entry(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StreamRequest.Entry]: ...
    def __init__(
        self,
        *,
        entry: collections.abc.Iterable[global___StreamRequest.Entry] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entry", b"entry"]) -> None: ...

global___StreamRequest = StreamRequest

@typing_extensions.final
class StreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Entry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSFER_FROM_FIELD_NUMBER: builtins.int
        COMPILE_FIELD_NUMBER: builtins.int
        STATUS_FIELD_NUMBER: builtins.int
        OPERATION_ID_FIELD_NUMBER: builtins.int
        @property
        def transfer_from(self) -> global___TransferFromDeviceResponse: ...
        @property
        def compile(self) -> global___CompileResponse: ...
        @property
        def status(self) -> global___StatusMessage: ...
        operation_id: builtins.int
        """Echos the given encoded EventId value."""
        def __init__(
            self,
            *,
            transfer_from: global___TransferFromDeviceResponse | None = ...,
            compile: global___CompileResponse | None = ...,
            status: global___StatusMessage | None = ...,
            operation_id: builtins.int | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["compile", b"compile", "operation_id", b"operation_id", "response", b"response", "status", b"status", "transfer_from", b"transfer_from"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["compile", b"compile", "operation_id", b"operation_id", "response", b"response", "status", b"status", "transfer_from", b"transfer_from"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["response", b"response"]) -> typing_extensions.Literal["transfer_from", "compile"] | None: ...

    ENTRY_FIELD_NUMBER: builtins.int
    @property
    def entry(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StreamResponse.Entry]: ...
    def __init__(
        self,
        *,
        entry: collections.abc.Iterable[global___StreamResponse.Entry] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entry", b"entry"]) -> None: ...

global___StreamResponse = StreamResponse

@typing_extensions.final
class OpenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    client_version: builtins.int
    """The version number for this client. Versions are bumped in case of
    backwards incompatible client-server protocol changes. Servers will reject
    clients with an unsupported version.
    """
    def __init__(
        self,
        *,
        client_version: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["client_version", b"client_version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_version", b"client_version"]) -> None: ...

global___OpenRequest = OpenRequest

@typing_extensions.final
class OpenResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    MAX_IDLE_TIME_SECONDS_FIELD_NUMBER: builtins.int
    client_id: builtins.int
    max_idle_time_seconds: builtins.int
    """Maximum time this client can be idle before it is GC'ed and all resources
    released.
    """
    def __init__(
        self,
        *,
        client_id: builtins.int | None = ...,
        max_idle_time_seconds: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "max_idle_time_seconds", b"max_idle_time_seconds"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "max_idle_time_seconds", b"max_idle_time_seconds"]) -> None: ...

global___OpenResponse = OpenResponse

@typing_extensions.final
class CloseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    client_id: builtins.int
    def __init__(
        self,
        *,
        client_id: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["client_id", b"client_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id"]) -> None: ...

global___CloseRequest = CloseRequest

@typing_extensions.final
class CloseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CloseResponse = CloseResponse

@typing_extensions.final
class ResetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ResetRequest = ResetRequest

@typing_extensions.final
class ResetResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ResetResponse = ResetResponse

@typing_extensions.final
class QuerySystemInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QuerySystemInfoRequest = QuerySystemInfoRequest

@typing_extensions.final
class QuerySystemInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SYSTEM_INFO_FIELD_NUMBER: builtins.int
    @property
    def system_info(self) -> tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2.SystemInfo: ...
    def __init__(
        self,
        *,
        system_info: tensorflow.compiler.xla.python.tpu_driver.tpu_driver_pb2.SystemInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["system_info", b"system_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["system_info", b"system_info"]) -> None: ...

global___QuerySystemInfoResponse = QuerySystemInfoResponse

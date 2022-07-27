"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.core.framework.tensor_pb2
import tensorflow.core.profiler.tfprof_log_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class EventReply(google.protobuf.message.Message):
    """Reply message from EventListener to the client, i.e., to the source of the
    Event protocol buffers, e.g., debug ops inserted by a debugged runtime to a
    TensorFlow graph being executed.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class DebugOpStateChange(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _State:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[EventReply.DebugOpStateChange._State.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            STATE_UNSPECIFIED: EventReply.DebugOpStateChange._State.ValueType  # 0
            DISABLED: EventReply.DebugOpStateChange._State.ValueType  # 1
            READ_ONLY: EventReply.DebugOpStateChange._State.ValueType  # 2
            READ_WRITE: EventReply.DebugOpStateChange._State.ValueType  # 3
        class State(_State, metaclass=_StateEnumTypeWrapper):
            pass

        STATE_UNSPECIFIED: EventReply.DebugOpStateChange.State.ValueType  # 0
        DISABLED: EventReply.DebugOpStateChange.State.ValueType  # 1
        READ_ONLY: EventReply.DebugOpStateChange.State.ValueType  # 2
        READ_WRITE: EventReply.DebugOpStateChange.State.ValueType  # 3

        STATE_FIELD_NUMBER: builtins.int
        NODE_NAME_FIELD_NUMBER: builtins.int
        OUTPUT_SLOT_FIELD_NUMBER: builtins.int
        DEBUG_OP_FIELD_NUMBER: builtins.int
        state: global___EventReply.DebugOpStateChange.State.ValueType
        node_name: typing.Text
        output_slot: builtins.int
        debug_op: typing.Text
        def __init__(self,
            *,
            state: global___EventReply.DebugOpStateChange.State.ValueType = ...,
            node_name: typing.Text = ...,
            output_slot: builtins.int = ...,
            debug_op: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["debug_op",b"debug_op","node_name",b"node_name","output_slot",b"output_slot","state",b"state"]) -> None: ...

    DEBUG_OP_STATE_CHANGES_FIELD_NUMBER: builtins.int
    TENSOR_FIELD_NUMBER: builtins.int
    @property
    def debug_op_state_changes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventReply.DebugOpStateChange]: ...
    @property
    def tensor(self) -> tensorflow.core.framework.tensor_pb2.TensorProto:
        """New tensor value to override the current tensor value with.
        TODO(cais): Make use of this field to implement overriding of tensor value
        during debugging.
        """
        pass
    def __init__(self,
        *,
        debug_op_state_changes: typing.Optional[typing.Iterable[global___EventReply.DebugOpStateChange]] = ...,
        tensor: typing.Optional[tensorflow.core.framework.tensor_pb2.TensorProto] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tensor",b"tensor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["debug_op_state_changes",b"debug_op_state_changes","tensor",b"tensor"]) -> None: ...
global___EventReply = EventReply

class CallTraceback(google.protobuf.message.Message):
    """Data on the traceback of a debugged call, e.g., a Session.run() call, or the
    execution of an eager operation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _CallType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _CallTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CallTraceback._CallType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: CallTraceback._CallType.ValueType  # 0
        GRAPH_EXECUTION: CallTraceback._CallType.ValueType  # 1
        EAGER_EXECUTION: CallTraceback._CallType.ValueType  # 2
    class CallType(_CallType, metaclass=_CallTypeEnumTypeWrapper):
        pass

    UNSPECIFIED: CallTraceback.CallType.ValueType  # 0
    GRAPH_EXECUTION: CallTraceback.CallType.ValueType  # 1
    EAGER_EXECUTION: CallTraceback.CallType.ValueType  # 2

    class OriginIdToStringEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: typing.Text
        def __init__(self,
            *,
            key: builtins.int = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    CALL_TYPE_FIELD_NUMBER: builtins.int
    CALL_KEY_FIELD_NUMBER: builtins.int
    ORIGIN_STACK_FIELD_NUMBER: builtins.int
    ORIGIN_ID_TO_STRING_FIELD_NUMBER: builtins.int
    GRAPH_TRACEBACK_FIELD_NUMBER: builtins.int
    GRAPH_VERSION_FIELD_NUMBER: builtins.int
    call_type: global___CallTraceback.CallType.ValueType
    call_key: typing.Text
    """A key for the call. For example, for graph execution, this is a key
    consisting of the names of the fed and fetched tensors.
    """

    @property
    def origin_stack(self) -> tensorflow.core.profiler.tfprof_log_pb2.CodeDef:
        """Traceback stack for the origin of the call event.
        For graph execution, this is the stack of the Session.run() call.
        For eager execution, this is the stack of the Python line that invokes
        the execution of the eager op.
        """
        pass
    @property
    def origin_id_to_string(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, typing.Text]:
        """Keeps track of the mapping from integer IDs in `origin_stack` to actual
        string values (e.g., file paths, function names).
        """
        pass
    @property
    def graph_traceback(self) -> tensorflow.core.profiler.tfprof_log_pb2.OpLogProto:
        """Traceback for the graph (if any) involved in the call."""
        pass
    graph_version: builtins.int
    """Version of the graph in `graph_traceback` (if any)."""

    def __init__(self,
        *,
        call_type: global___CallTraceback.CallType.ValueType = ...,
        call_key: typing.Text = ...,
        origin_stack: typing.Optional[tensorflow.core.profiler.tfprof_log_pb2.CodeDef] = ...,
        origin_id_to_string: typing.Optional[typing.Mapping[builtins.int, typing.Text]] = ...,
        graph_traceback: typing.Optional[tensorflow.core.profiler.tfprof_log_pb2.OpLogProto] = ...,
        graph_version: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["graph_traceback",b"graph_traceback","origin_stack",b"origin_stack"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["call_key",b"call_key","call_type",b"call_type","graph_traceback",b"graph_traceback","graph_version",b"graph_version","origin_id_to_string",b"origin_id_to_string","origin_stack",b"origin_stack"]) -> None: ...
global___CallTraceback = CallTraceback

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

class _VariableSynchronization:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VariableSynchronizationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VariableSynchronization.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VARIABLE_SYNCHRONIZATION_AUTO: _VariableSynchronization.ValueType  # 0
    """`AUTO`: Indicates that the synchronization will be determined by the
    current `DistributionStrategy` (eg. With `MirroredStrategy` this would be
    `ON_WRITE`).
    """

    VARIABLE_SYNCHRONIZATION_NONE: _VariableSynchronization.ValueType  # 1
    """`NONE`: Indicates that there will only be one copy of the variable, so
    there is no need to sync.
    """

    VARIABLE_SYNCHRONIZATION_ON_WRITE: _VariableSynchronization.ValueType  # 2
    """`ON_WRITE`: Indicates that the variable will be updated across devices
    every time it is written.
    """

    VARIABLE_SYNCHRONIZATION_ON_READ: _VariableSynchronization.ValueType  # 3
    """`ON_READ`: Indicates that the variable will be aggregated across devices
    when it is read (eg. when checkpointing or when evaluating an op that uses
    the variable).
    """

class VariableSynchronization(_VariableSynchronization, metaclass=_VariableSynchronizationEnumTypeWrapper):
    """Indicates when a distributed variable will be synced."""
    pass

VARIABLE_SYNCHRONIZATION_AUTO: VariableSynchronization.ValueType  # 0
"""`AUTO`: Indicates that the synchronization will be determined by the
current `DistributionStrategy` (eg. With `MirroredStrategy` this would be
`ON_WRITE`).
"""

VARIABLE_SYNCHRONIZATION_NONE: VariableSynchronization.ValueType  # 1
"""`NONE`: Indicates that there will only be one copy of the variable, so
there is no need to sync.
"""

VARIABLE_SYNCHRONIZATION_ON_WRITE: VariableSynchronization.ValueType  # 2
"""`ON_WRITE`: Indicates that the variable will be updated across devices
every time it is written.
"""

VARIABLE_SYNCHRONIZATION_ON_READ: VariableSynchronization.ValueType  # 3
"""`ON_READ`: Indicates that the variable will be aggregated across devices
when it is read (eg. when checkpointing or when evaluating an op that uses
the variable).
"""

global___VariableSynchronization = VariableSynchronization


class _VariableAggregation:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VariableAggregationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VariableAggregation.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VARIABLE_AGGREGATION_NONE: _VariableAggregation.ValueType  # 0
    """`NONE`: This is the default, giving an error if you use a
    variable-update operation with multiple replicas.
    """

    VARIABLE_AGGREGATION_SUM: _VariableAggregation.ValueType  # 1
    """`SUM`: Add the updates across replicas."""

    VARIABLE_AGGREGATION_MEAN: _VariableAggregation.ValueType  # 2
    """`MEAN`: Take the arithmetic mean ("average") of the updates across
    replicas.
    """

    VARIABLE_AGGREGATION_ONLY_FIRST_REPLICA: _VariableAggregation.ValueType  # 3
    """`ONLY_FIRST_REPLICA`: This is for when every replica is performing the same
    update, but we only want to perform the update once. Used, e.g., for the
    global step counter.
    """

class VariableAggregation(_VariableAggregation, metaclass=_VariableAggregationEnumTypeWrapper):
    """Indicates how a distributed variable will be aggregated."""
    pass

VARIABLE_AGGREGATION_NONE: VariableAggregation.ValueType  # 0
"""`NONE`: This is the default, giving an error if you use a
variable-update operation with multiple replicas.
"""

VARIABLE_AGGREGATION_SUM: VariableAggregation.ValueType  # 1
"""`SUM`: Add the updates across replicas."""

VARIABLE_AGGREGATION_MEAN: VariableAggregation.ValueType  # 2
"""`MEAN`: Take the arithmetic mean ("average") of the updates across
replicas.
"""

VARIABLE_AGGREGATION_ONLY_FIRST_REPLICA: VariableAggregation.ValueType  # 3
"""`ONLY_FIRST_REPLICA`: This is for when every replica is performing the same
update, but we only want to perform the update once. Used, e.g., for the
global step counter.
"""

global___VariableAggregation = VariableAggregation


class VariableDef(google.protobuf.message.Message):
    """Protocol buffer representing a Variable."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VARIABLE_NAME_FIELD_NUMBER: builtins.int
    INITIAL_VALUE_NAME_FIELD_NUMBER: builtins.int
    INITIALIZER_NAME_FIELD_NUMBER: builtins.int
    SNAPSHOT_NAME_FIELD_NUMBER: builtins.int
    SAVE_SLICE_INFO_DEF_FIELD_NUMBER: builtins.int
    IS_RESOURCE_FIELD_NUMBER: builtins.int
    TRAINABLE_FIELD_NUMBER: builtins.int
    SYNCHRONIZATION_FIELD_NUMBER: builtins.int
    AGGREGATION_FIELD_NUMBER: builtins.int
    variable_name: typing.Text
    """Name of the variable tensor."""

    initial_value_name: typing.Text
    """Name of the tensor holding the variable's initial value."""

    initializer_name: typing.Text
    """Name of the initializer op."""

    snapshot_name: typing.Text
    """Name of the snapshot tensor."""

    @property
    def save_slice_info_def(self) -> global___SaveSliceInfoDef:
        """Support for saving variables as slices of a larger variable."""
        pass
    is_resource: builtins.bool
    """Whether to represent this as a ResourceVariable."""

    trainable: builtins.bool
    """Whether this variable should be trained."""

    synchronization: global___VariableSynchronization.ValueType
    """Indicates when a distributed variable will be synced."""

    aggregation: global___VariableAggregation.ValueType
    """Indicates how a distributed variable will be aggregated."""

    def __init__(self,
        *,
        variable_name: typing.Text = ...,
        initial_value_name: typing.Text = ...,
        initializer_name: typing.Text = ...,
        snapshot_name: typing.Text = ...,
        save_slice_info_def: typing.Optional[global___SaveSliceInfoDef] = ...,
        is_resource: builtins.bool = ...,
        trainable: builtins.bool = ...,
        synchronization: global___VariableSynchronization.ValueType = ...,
        aggregation: global___VariableAggregation.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["save_slice_info_def",b"save_slice_info_def"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregation",b"aggregation","initial_value_name",b"initial_value_name","initializer_name",b"initializer_name","is_resource",b"is_resource","save_slice_info_def",b"save_slice_info_def","snapshot_name",b"snapshot_name","synchronization",b"synchronization","trainable",b"trainable","variable_name",b"variable_name"]) -> None: ...
global___VariableDef = VariableDef

class SaveSliceInfoDef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FULL_NAME_FIELD_NUMBER: builtins.int
    FULL_SHAPE_FIELD_NUMBER: builtins.int
    VAR_OFFSET_FIELD_NUMBER: builtins.int
    VAR_SHAPE_FIELD_NUMBER: builtins.int
    full_name: typing.Text
    """Name of the full variable of which this is a slice."""

    @property
    def full_shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Shape of the full variable."""
        pass
    @property
    def var_offset(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Offset of this variable into the full variable."""
        pass
    @property
    def var_shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Shape of this variable."""
        pass
    def __init__(self,
        *,
        full_name: typing.Text = ...,
        full_shape: typing.Optional[typing.Iterable[builtins.int]] = ...,
        var_offset: typing.Optional[typing.Iterable[builtins.int]] = ...,
        var_shape: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["full_name",b"full_name","full_shape",b"full_shape","var_offset",b"var_offset","var_shape",b"var_shape"]) -> None: ...
global___SaveSliceInfoDef = SaveSliceInfoDef

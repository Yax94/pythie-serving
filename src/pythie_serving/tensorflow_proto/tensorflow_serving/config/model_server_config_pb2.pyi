"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import tensorflow_serving.config.file_system_storage_path_source_pb2
import tensorflow_serving.config.logging_config_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ModelType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ModelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ModelType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MODEL_TYPE_UNSPECIFIED: _ModelType.ValueType  # 0
    TENSORFLOW: _ModelType.ValueType  # 1
    OTHER: _ModelType.ValueType  # 2

class ModelType(_ModelType, metaclass=_ModelTypeEnumTypeWrapper):
    """The type of model.
    TODO(b/31336131): DEPRECATED.
    """

MODEL_TYPE_UNSPECIFIED: ModelType.ValueType  # 0
TENSORFLOW: ModelType.ValueType  # 1
OTHER: ModelType.ValueType  # 2
global___ModelType = ModelType

@typing_extensions.final
class ModelConfig(google.protobuf.message.Message):
    """Common configuration for loading a model being served."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class VersionLabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    BASE_PATH_FIELD_NUMBER: builtins.int
    MODEL_TYPE_FIELD_NUMBER: builtins.int
    MODEL_PLATFORM_FIELD_NUMBER: builtins.int
    MODEL_VERSION_POLICY_FIELD_NUMBER: builtins.int
    VERSION_LABELS_FIELD_NUMBER: builtins.int
    LOGGING_CONFIG_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the model."""
    base_path: builtins.str
    """Base path to the model, excluding the version directory.
    E.g> for a model at /foo/bar/my_model/123, where 123 is the version, the
    base path is /foo/bar/my_model.

    (This can be changed once a model is in serving, *if* the underlying data
    remains the same. Otherwise there are no guarantees about whether the old
    or new data will be used for model versions currently loaded.)
    """
    model_type: global___ModelType.ValueType
    """Type of model.
    TODO(b/31336131): DEPRECATED. Please use 'model_platform' instead.
    """
    model_platform: builtins.str
    """Type of model (e.g. "tensorflow").

    (This cannot be changed once a model is in serving.)
    """
    @property
    def model_version_policy(self) -> tensorflow_serving.config.file_system_storage_path_source_pb2.FileSystemStoragePathSourceConfig.ServableVersionPolicy:
        """Version policy for the model indicating which version(s) of the model to
        load and make available for serving simultaneously.
        The default option is to serve only the latest version of the model.

        (This can be changed once a model is in serving.)
        """
    @property
    def version_labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """String labels to associate with versions of the model, allowing inference
        queries to refer to versions by label instead of number. Multiple labels
        can map to the same version, but not vice-versa.

        An envisioned use-case for these labels is canarying tentative versions.
        For example, one can assign labels "stable" and "canary" to two specific
        versions. Perhaps initially "stable" is assigned to version 0 and "canary"
        to version 1. Once version 1 passes canary, one can shift the "stable"
        label to refer to version 1 (at that point both labels map to the same
        version -- version 1 -- which is fine). Later once version 2 is ready to
        canary one can move the "canary" label to version 2. And so on.
        """
    @property
    def logging_config(self) -> tensorflow_serving.config.logging_config_pb2.LoggingConfig:
        """Configures logging requests and responses, to the model.

        (This can be changed once a model is in serving.)
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        base_path: builtins.str = ...,
        model_type: global___ModelType.ValueType = ...,
        model_platform: builtins.str = ...,
        model_version_policy: tensorflow_serving.config.file_system_storage_path_source_pb2.FileSystemStoragePathSourceConfig.ServableVersionPolicy | None = ...,
        version_labels: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
        logging_config: tensorflow_serving.config.logging_config_pb2.LoggingConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["logging_config", b"logging_config", "model_version_policy", b"model_version_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_path", b"base_path", "logging_config", b"logging_config", "model_platform", b"model_platform", "model_type", b"model_type", "model_version_policy", b"model_version_policy", "name", b"name", "version_labels", b"version_labels"]) -> None: ...

global___ModelConfig = ModelConfig

@typing_extensions.final
class ModelConfigList(google.protobuf.message.Message):
    """Static list of models to be loaded for serving."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModelConfig]: ...
    def __init__(
        self,
        *,
        config: collections.abc.Iterable[global___ModelConfig] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config"]) -> None: ...

global___ModelConfigList = ModelConfigList

@typing_extensions.final
class ModelServerConfig(google.protobuf.message.Message):
    """ModelServer config."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_CONFIG_LIST_FIELD_NUMBER: builtins.int
    CUSTOM_MODEL_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def model_config_list(self) -> global___ModelConfigList: ...
    @property
    def custom_model_config(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        model_config_list: global___ModelConfigList | None = ...,
        custom_model_config: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config", "custom_model_config", b"custom_model_config", "model_config_list", b"model_config_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "custom_model_config", b"custom_model_config", "model_config_list", b"model_config_list"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["model_config_list", "custom_model_config"] | None: ...

global___ModelServerConfig = ModelServerConfig

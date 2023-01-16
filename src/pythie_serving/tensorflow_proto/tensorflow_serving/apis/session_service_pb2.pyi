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
import tensorflow.core.protobuf.config_pb2
import tensorflow.core.protobuf.named_tensor_pb2
import tensorflow_serving.apis.model_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SessionRunRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_SPEC_FIELD_NUMBER: builtins.int
    FEED_FIELD_NUMBER: builtins.int
    FETCH_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    TENSOR_NAME_IS_ALIAS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def model_spec(self) -> tensorflow_serving.apis.model_pb2.ModelSpec:
        """Model Specification. If version is not specified, will use the latest
        (numerical) version.
        """
    @property
    def feed(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.protobuf.named_tensor_pb2.NamedTensorProto]:
        """Tensors to be fed in the step. Each feed is a named tensor."""
    @property
    def fetch(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Fetches. A list of tensor names. The caller expects a tensor to
        be returned for each fetch[i] (see RunResponse.tensor). The
        order of specified fetches does not change the execution order.
        """
    @property
    def target(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Target Nodes. A list of node names. The named nodes will be run
        to but their outputs will not be fetched.
        """
    tensor_name_is_alias: builtins.bool
    """If true, treat names in feed/fetch/target as alias names than actual tensor
    names (that appear in the TF graph). Alias names are resolved to actual
    names using `SignatureDef` in SavedModel associated with the model.
    """
    @property
    def options(self) -> tensorflow.core.protobuf.config_pb2.RunOptions:
        """Options for the run call. **Currently ignored.**"""
    def __init__(
        self,
        *,
        model_spec: tensorflow_serving.apis.model_pb2.ModelSpec | None = ...,
        feed: collections.abc.Iterable[tensorflow.core.protobuf.named_tensor_pb2.NamedTensorProto] | None = ...,
        fetch: collections.abc.Iterable[builtins.str] | None = ...,
        target: collections.abc.Iterable[builtins.str] | None = ...,
        tensor_name_is_alias: builtins.bool = ...,
        options: tensorflow.core.protobuf.config_pb2.RunOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model_spec", b"model_spec", "options", b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feed", b"feed", "fetch", b"fetch", "model_spec", b"model_spec", "options", b"options", "target", b"target", "tensor_name_is_alias", b"tensor_name_is_alias"]) -> None: ...

global___SessionRunRequest = SessionRunRequest

@typing_extensions.final
class SessionRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_SPEC_FIELD_NUMBER: builtins.int
    TENSOR_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    @property
    def model_spec(self) -> tensorflow_serving.apis.model_pb2.ModelSpec:
        """Effective Model Specification used for session run."""
    @property
    def tensor(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.protobuf.named_tensor_pb2.NamedTensorProto]:
        """NOTE: The order of the returned tensors may or may not match
        the fetch order specified in RunRequest.
        """
    @property
    def metadata(self) -> tensorflow.core.protobuf.config_pb2.RunMetadata:
        """Returned metadata if requested in the options."""
    def __init__(
        self,
        *,
        model_spec: tensorflow_serving.apis.model_pb2.ModelSpec | None = ...,
        tensor: collections.abc.Iterable[tensorflow.core.protobuf.named_tensor_pb2.NamedTensorProto] | None = ...,
        metadata: tensorflow.core.protobuf.config_pb2.RunMetadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "model_spec", b"model_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "model_spec", b"model_spec", "tensor", b"tensor"]) -> None: ...

global___SessionRunResponse = SessionRunResponse

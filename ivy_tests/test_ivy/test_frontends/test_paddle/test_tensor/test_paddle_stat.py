# global
from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test
from ivy_tests.test_ivy.test_functional.test_core.test_statistical import (
    _statistical_dtype_values,
)


# mean
@handle_frontend_test(
    fn_tree="paddle.mean",
    dtype_and_x=_statistical_dtype_values(function="mean"),
    keepdims=st.booleans(),
)
def test_paddle_mean(
    *,
    dtype_and_x,
    keepdims,
    on_device,
    fn_tree,
    frontend,
    test_flags,
):
    input_dtype, x, axis = dtype_and_x
    helpers.test_frontend_function(
        input_dtypes=input_dtype,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        input=x[0],
        axis=axis,
        keepdims=keepdims,
    )


# numel
@handle_frontend_test(
    fn_tree="paddle.numel",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("valid"),
        min_num_dims=1,
    ),
)
def test_paddle_numel(
    *,
    dtype_and_x,
    on_device,
    fn_tree,
    frontend,
    test_flags,
):
    input_dtype, x = dtype_and_x
    helpers.test_frontend_function(
        input_dtypes=input_dtype,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        input=x[0],
    )

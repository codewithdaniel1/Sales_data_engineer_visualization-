from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

# Import the names of callback functions you want to test
from visualization import update_chart

def test_update_chart_callback_all():
    # Test with 'all' selected
    output = update_chart('all')
    assert output.layout.title.text == "Pink Morsel Sales Trend for All Regions"

def test_update_chart_callback_north():
    # Test with 'north' selected
    output = update_chart('north')
    assert output.layout.title.text == "Pink Morsel Sales Trend for North Region"

def test_region_picker_callback():
    def run_callback():
        # Simulate a selection of 'north' in the region picker
        context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": "region-filter.value"}]}))
        return update_chart('north')

    # Use context to simulate Dash's callback context and test callback functionality
    ctx = copy_context()
    output = ctx.run(run_callback)
    assert output.layout.title.text == "Pink Morsel Sales Trend for North Region"

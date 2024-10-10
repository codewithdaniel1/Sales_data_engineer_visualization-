from visualization import update_chart  # Import update_chart from visualization.py

# Test cases for different regions and products
def test_update_chart_callback_all_all():
    # Test with 'all' selected for both region and product
    output = update_chart('all', 'all')
    assert output.layout.title.text == "Sales Trend"

def test_update_chart_callback_north_pink_morsel():
    # Test with 'north' region and 'pink morsel' product selected
    output = update_chart('north', 'pink morsel')
    assert output.layout.title.text == "Sales Trend for Pink morsel in North Region"

def test_update_chart_callback_south_gold_morsel():
    # Test with 'south' region and 'gold morsel' product selected
    output = update_chart('south', 'gold morsel')
    assert output.layout.title.text == "Sales Trend for Gold morsel in South Region"

def test_update_chart_callback_west_vermilion_morsel():
    # Test with 'west' region and 'vermilion morsel' product selected
    output = update_chart('west', 'vermilion morsel')
    assert output.layout.title.text == "Sales Trend for Vermilion morsel in West Region"

def test_update_chart_callback_east_chartreuse_morsel():
    # Test with 'east' region and 'chartreuse morsel' product selected
    output = update_chart('east', 'chartreuse morsel')
    assert output.layout.title.text == "Sales Trend for Chartreuse morsel in East Region"

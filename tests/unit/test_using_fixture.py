def test_using_fixture(sample_data):
    assert sample_data["value"] == 42

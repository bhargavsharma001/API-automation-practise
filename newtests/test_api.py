import os
import time

import pytest
import config_setup

ids=[f"TESTCASE-{i}" for i in range(1,len(config_setup.fetch_data())+1)]

@pytest.mark.parametrize("From,To,estimated_diameter_max,estimated_diameter_min",config_setup.fetch_data(),ids=ids)
def test_validate_api(From,To,estimated_diameter_max,estimated_diameter_min):
    resp=config_setup.setup(From,To)
    assert resp.get("estimated_diameter_max")==estimated_diameter_max
    assert resp.get("estimated_diameter_min")==estimated_diameter_min

@pytest.mark.parametrize("question,expected",config_setup.fetch_data_gemini())
def test_gemini_api(question,expected):
    API_KEY = os.getenv("GEMINI_API_KEY")
    response=config_setup.gemini_api(API_KEY,question)
    val= response.json().get('candidates')[0].get("content").get("parts")[0].get('text')
    assert response.status_code==200,"invalid status code "
    assert expected in val
    time.sleep(1)


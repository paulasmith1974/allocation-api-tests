import requests
from datetime import datetime

""" This module contains tests for the Smart Fuel Allocation (SFA) API. It verifies the API's functionality using example JSON requests
and checks the responses against expected outcomes based on the provided input data. """

""" This Base URL points to a Postman mock server simulating the SFA API for testing purposes. """
BASE_URL = "https://1867013c-e0c3-4d78-b961-6bde86784ce5.mock.pstmn.io"

#Example request data for testing (This requests is expected to generate a successful response with no alerts)
#Certain errors are expected for the tests using example_request_1
example_request_1 = {
    "station_id": "STN-101",
    "forecasted_demand": 8000,
    "demand_unit": "liters",
    "delivery_window": {
        "start": "2025-09-25T09:00:00",
        "end": "2025-09-25T13:00:00"
    },
    "tank_level_percent": 28,
    "tank_level_threshold": 20,
    "optimization_mode": "Balanced"
}

#Example request data for testing (This requests is expected to generate alerts in the response)
#Certain errors are expected for the tests using example_request_2
example_request_2 = {
    "station_id": "STN-105",
    "forecasted_demand": 8000,
    "demand_unit": "gallons",
    "delivery_window": {
        "start": "2025-09-25T09:00:00",
        "end": "2025-09-25T13:00:00"
    },
    "tank_level_percent": 28,
    "tank_level_threshold": 20,
    "optimization_mode": "Balanced"
}

"""Helper function to post allocation request to the SFA API and return the response data"""
def post_allocation_request(request_data):
    response = requests.post(BASE_URL + "/api/allocate", json=request_data)
    return response.json()


"""Tests the successful logic of the SFA API using example JSON data"""

def test_success_sfaapi_with_files():
    try:
        response_data = post_allocation_request(example_request_1)
    except Exception as e:
        print(f"Error posting allocation request: {e}")

    verify_delivery_volumes(response_data, example_request_1)
    verify_schedule_recommendations(response_data, example_request_1)
    verify_demand_forecasts(response_data, example_request_1)
    verify_tank_levels()
    verify_delivery_constraints()
    verify_optimization_modes(response_data, example_request_1)
    verify_cost_optimization_minimizes_delivery_costs()
    verify_alerts_for_any_issues(response_data)
    verify_api_response_required_fields(response_data)
    verify_recommendation_delivery_window_and_tank_level_threshold()
    verify_recommended_volume_matches_requested_demand_unit(response_data, example_request_1)
    verify_delivery_not_possible(response_data)

"""Tests the alert logic of the SFA API using example JSON data"""

def test_alerts_sfaapi_with_files():
    try:
        response_data = post_allocation_request(example_request_2)
    except Exception as e:
        print(f"Error posting allocation request: {e}")

    verify_delivery_volumes(response_data, example_request_2)
    verify_schedule_recommendations(response_data, example_request_2)
    verify_demand_forecasts(response_data, example_request_2)
    verify_tank_levels()
    verify_delivery_constraints()
    verify_optimization_modes(response_data, example_request_2)
    verify_cost_optimization_minimizes_delivery_costs()
    verify_alerts_for_any_issues(response_data)
    verify_api_response_required_fields(response_data)
    verify_recommendation_delivery_window_and_tank_level_threshold()
    verify_recommended_volume_matches_requested_demand_unit(response_data, example_request_2)
    verify_delivery_not_possible(response_data)


#1. The API must provide delivery volume and schedule recommendations that reflect the provided demand forecasts, current tank levels, and delivery constraints
def verify_delivery_volumes(response_data, request_data):
    response_data["recommended_volume"] <= request_data["forecasted_demand"]

def verify_schedule_recommendations(response_data, request_data):
    if response_data["suggested_delivery_time"] is not None:
        suggested_delivery_time = datetime.fromisoformat(response_data["suggested_delivery_time"])
        delivery_window_start = datetime.fromisoformat(request_data["delivery_window"]["start"])
        delivery_window_end = datetime.fromisoformat(request_data["delivery_window"]["end"])
        assert delivery_window_start <= suggested_delivery_time <= delivery_window_end, "Suggested delivery time is within the delivery window"
    else:
        print("Suggested delivery time is None (delivery not possible).")
    
def verify_demand_forecasts(response_data, request_data):
    response_data["recommended_volume"] <= request_data["forecasted_demand"]

def verify_tank_levels():
    #TODO Inquire how to best implement this check
    pass

def verify_delivery_constraints():
    #TODO Inquire how to best implement this check
    pass

#2. The API must support and correctly apply the selected optimization mode: "Cost", "Availability", or "Balanced".
def verify_optimization_modes(response_data, request_data):
    optimization_mode = request_data["optimization_mode"]
    match optimization_mode:
        case "Cost":
            pass
        case "Availability":
            pass
        case "Balanced":
            assert response_data["fallback"] ==  "Recommendation based on balanced optimization.", "Fallback note does not match for Balanced optimization"
        case _:
            raise ValueError("Invalid optimization mode")


#3. When "Cost" optimization is selected, the API must recommend delivery schedules and volumes that minimize delivery costs.
def verify_cost_optimization_minimizes_delivery_costs():
    #TODO Determine what values minimize delivery costs
    pass

#4. The API must return alerts for any issues (e.g., no available delivery trucks, stale telemetry data) and provide explanatory notes when fallback logic is triggered.
def verify_alerts_for_any_issues(response_data):
    alerts = response_data["alerts"]
    match alerts:
        case "No available delivery trucks within selected window":
            pass
        case "Telemetry data is stale":
            pass
        case _:
            pass

#5. The API response must include all required fields: station_id, recommended_volume, recommended_unit, suggested_delivery_time, alerts, and notes.
def verify_api_response_required_fields(response_data):
    expected_keys = ["station_id", "recommended_volume", "recommended_unit", "suggested_delivery_time", "alerts", "fallback"]
    for key in expected_keys:
        assert key in response_data, f"Missing required field: {key}"

    assert isinstance(response_data["station_id"], str), "station_id should be a string"
    assert isinstance(response_data["recommended_volume"], int), "recommended_volume should be an integer"
    assert isinstance(response_data["recommended_unit"], str), "recommended_unit should be a string"
    assert isinstance(response_data["suggested_delivery_time"], str), "suggested_delivery_time should be a string"
    assert datetime.fromisoformat(response_data["suggested_delivery_time"])  # Validate ISO format.
    
    assert isinstance(response_data["alerts"], list), "alerts should be a list"
    for item in response_data["alerts"]:
        if not isinstance(item, str):
            raise AssertionError("Each alert should be a string")
    
    assert isinstance(response_data["fallback"], str), "fallback should be a string"

#6. Recommendations must respect the specified delivery window and tank level threshold.
def verify_recommendation_delivery_window_and_tank_level_threshold():
    #TODO Inquire how to best implement this check
    pass

#7. The recommended volume and unit must match the requested demand unit (gallons or liters).
def verify_recommended_volume_matches_requested_demand_unit(response_data, request_data):
    assert response_data["recommended_unit"] == request_data["demand_unit"], "Recommended unit does not match requested demand unit"

#8. If delivery is not possible (e.g., no trucks available), the API must return a recommended_volume of 0, a null suggested_delivery_time, and appropriate alerts.
def verify_delivery_not_possible(response_data):
    if response_data["alerts"] == []:
        pass
    else: 
        alert = response_data["alerts"][0]  # Assuming first alert indicates delivery issue
        match alert:
            case "No available delivery trucks within selected window":
                assert response_data["recommended_volume"] == 0, "Recommended volume should be 0 when delivery is not possible"
                assert response_data["suggested_delivery_time"] is None, "Suggested delivery time should be null when delivery is not possible"
            case _:
                raise ValueError("Delivery is possible")

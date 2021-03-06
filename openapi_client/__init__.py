# coding: utf-8

# flake8: noqa

"""
    MBTA

    MBTA service API. https://www.mbta.com Source code: https://github.com/mbta/api  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: developer@mbta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.alert_api import AlertApi
from openapi_client.api.facility_api import FacilityApi
from openapi_client.api.line_api import LineApi
from openapi_client.api.live_facility_api import LiveFacilityApi
from openapi_client.api.prediction_api import PredictionApi
from openapi_client.api.route_api import RouteApi
from openapi_client.api.route_pattern_api import RoutePatternApi
from openapi_client.api.schedule_api import ScheduleApi
from openapi_client.api.service_api import ServiceApi
from openapi_client.api.shape_api import ShapeApi
from openapi_client.api.stop_api import StopApi
from openapi_client.api.trip_api import TripApi
from openapi_client.api.vehicle_api import VehicleApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.active_period import ActivePeriod
from openapi_client.models.alert import Alert
from openapi_client.models.alert_resource import AlertResource
from openapi_client.models.alert_resource_attributes import AlertResourceAttributes
from openapi_client.models.alert_resource_relationships import AlertResourceRelationships
from openapi_client.models.alert_resource_relationships_facility import AlertResourceRelationshipsFacility
from openapi_client.models.alert_resource_relationships_facility_data import AlertResourceRelationshipsFacilityData
from openapi_client.models.alert_resource_relationships_facility_links import AlertResourceRelationshipsFacilityLinks
from openapi_client.models.alerts import Alerts
from openapi_client.models.bad_request import BadRequest
from openapi_client.models.bad_request_errors import BadRequestErrors
from openapi_client.models.bad_request_source import BadRequestSource
from openapi_client.models.facilities import Facilities
from openapi_client.models.facility import Facility
from openapi_client.models.facility_property import FacilityProperty
from openapi_client.models.facility_resource import FacilityResource
from openapi_client.models.facility_resource_attributes import FacilityResourceAttributes
from openapi_client.models.facility_resource_relationships import FacilityResourceRelationships
from openapi_client.models.forbidden import Forbidden
from openapi_client.models.forbidden_errors import ForbiddenErrors
from openapi_client.models.informed_entity import InformedEntity
from openapi_client.models.line import Line
from openapi_client.models.line_resource import LineResource
from openapi_client.models.line_resource_attributes import LineResourceAttributes
from openapi_client.models.lines import Lines
from openapi_client.models.live_facilities import LiveFacilities
from openapi_client.models.live_facility import LiveFacility
from openapi_client.models.live_facility_resource import LiveFacilityResource
from openapi_client.models.live_facility_resource_attributes import LiveFacilityResourceAttributes
from openapi_client.models.not_found import NotFound
from openapi_client.models.not_found_errors import NotFoundErrors
from openapi_client.models.not_found_source import NotFoundSource
from openapi_client.models.prediction_resource import PredictionResource
from openapi_client.models.prediction_resource_attributes import PredictionResourceAttributes
from openapi_client.models.prediction_resource_relationships import PredictionResourceRelationships
from openapi_client.models.prediction_resource_relationships_alerts import PredictionResourceRelationshipsAlerts
from openapi_client.models.prediction_resource_relationships_alerts_data import PredictionResourceRelationshipsAlertsData
from openapi_client.models.prediction_resource_relationships_alerts_links import PredictionResourceRelationshipsAlertsLinks
from openapi_client.models.prediction_resource_relationships_route import PredictionResourceRelationshipsRoute
from openapi_client.models.prediction_resource_relationships_route_data import PredictionResourceRelationshipsRouteData
from openapi_client.models.prediction_resource_relationships_route_links import PredictionResourceRelationshipsRouteLinks
from openapi_client.models.prediction_resource_relationships_schedule import PredictionResourceRelationshipsSchedule
from openapi_client.models.prediction_resource_relationships_schedule_data import PredictionResourceRelationshipsScheduleData
from openapi_client.models.prediction_resource_relationships_schedule_links import PredictionResourceRelationshipsScheduleLinks
from openapi_client.models.prediction_resource_relationships_stop import PredictionResourceRelationshipsStop
from openapi_client.models.prediction_resource_relationships_stop_data import PredictionResourceRelationshipsStopData
from openapi_client.models.prediction_resource_relationships_stop_links import PredictionResourceRelationshipsStopLinks
from openapi_client.models.prediction_resource_relationships_trip import PredictionResourceRelationshipsTrip
from openapi_client.models.prediction_resource_relationships_trip_data import PredictionResourceRelationshipsTripData
from openapi_client.models.prediction_resource_relationships_trip_links import PredictionResourceRelationshipsTripLinks
from openapi_client.models.prediction_resource_relationships_vehicle import PredictionResourceRelationshipsVehicle
from openapi_client.models.prediction_resource_relationships_vehicle_data import PredictionResourceRelationshipsVehicleData
from openapi_client.models.prediction_resource_relationships_vehicle_links import PredictionResourceRelationshipsVehicleLinks
from openapi_client.models.predictions import Predictions
from openapi_client.models.route import Route
from openapi_client.models.route_pattern import RoutePattern
from openapi_client.models.route_pattern_resource import RoutePatternResource
from openapi_client.models.route_pattern_resource_attributes import RoutePatternResourceAttributes
from openapi_client.models.route_pattern_resource_relationships import RoutePatternResourceRelationships
from openapi_client.models.route_pattern_resource_relationships_representative_trip import RoutePatternResourceRelationshipsRepresentativeTrip
from openapi_client.models.route_pattern_resource_relationships_representative_trip_data import RoutePatternResourceRelationshipsRepresentativeTripData
from openapi_client.models.route_pattern_resource_relationships_representative_trip_links import RoutePatternResourceRelationshipsRepresentativeTripLinks
from openapi_client.models.route_patterns import RoutePatterns
from openapi_client.models.route_resource import RouteResource
from openapi_client.models.route_resource_attributes import RouteResourceAttributes
from openapi_client.models.routes import Routes
from openapi_client.models.schedule_resource import ScheduleResource
from openapi_client.models.schedule_resource_attributes import ScheduleResourceAttributes
from openapi_client.models.schedule_resource_relationships import ScheduleResourceRelationships
from openapi_client.models.schedule_resource_relationships_prediction import ScheduleResourceRelationshipsPrediction
from openapi_client.models.schedule_resource_relationships_prediction_data import ScheduleResourceRelationshipsPredictionData
from openapi_client.models.schedule_resource_relationships_prediction_links import ScheduleResourceRelationshipsPredictionLinks
from openapi_client.models.schedules import Schedules
from openapi_client.models.schedules_links import SchedulesLinks
from openapi_client.models.service import Service
from openapi_client.models.service_included import ServiceIncluded
from openapi_client.models.service_links import ServiceLinks
from openapi_client.models.service_resource import ServiceResource
from openapi_client.models.service_resource_attributes import ServiceResourceAttributes
from openapi_client.models.services import Services
from openapi_client.models.shape import Shape
from openapi_client.models.shape_resource import ShapeResource
from openapi_client.models.shape_resource_attributes import ShapeResourceAttributes
from openapi_client.models.shape_resource_relationships import ShapeResourceRelationships
from openapi_client.models.shape_resource_relationships_stops import ShapeResourceRelationshipsStops
from openapi_client.models.shape_resource_relationships_stops_data import ShapeResourceRelationshipsStopsData
from openapi_client.models.shape_resource_relationships_stops_links import ShapeResourceRelationshipsStopsLinks
from openapi_client.models.shapes import Shapes
from openapi_client.models.stop import Stop
from openapi_client.models.stop_resource import StopResource
from openapi_client.models.stop_resource_attributes import StopResourceAttributes
from openapi_client.models.stop_resource_relationships import StopResourceRelationships
from openapi_client.models.stop_resource_relationships_parent_station import StopResourceRelationshipsParentStation
from openapi_client.models.stop_resource_relationships_parent_station_data import StopResourceRelationshipsParentStationData
from openapi_client.models.stop_resource_relationships_parent_station_links import StopResourceRelationshipsParentStationLinks
from openapi_client.models.stops import Stops
from openapi_client.models.too_many_requests import TooManyRequests
from openapi_client.models.too_many_requests_errors import TooManyRequestsErrors
from openapi_client.models.trip import Trip
from openapi_client.models.trip_resource import TripResource
from openapi_client.models.trip_resource_attributes import TripResourceAttributes
from openapi_client.models.trip_resource_relationships import TripResourceRelationships
from openapi_client.models.trip_resource_relationships_route_pattern import TripResourceRelationshipsRoutePattern
from openapi_client.models.trip_resource_relationships_route_pattern_data import TripResourceRelationshipsRoutePatternData
from openapi_client.models.trip_resource_relationships_route_pattern_links import TripResourceRelationshipsRoutePatternLinks
from openapi_client.models.trip_resource_relationships_service import TripResourceRelationshipsService
from openapi_client.models.trip_resource_relationships_service_data import TripResourceRelationshipsServiceData
from openapi_client.models.trip_resource_relationships_service_links import TripResourceRelationshipsServiceLinks
from openapi_client.models.trip_resource_relationships_shape import TripResourceRelationshipsShape
from openapi_client.models.trip_resource_relationships_shape_data import TripResourceRelationshipsShapeData
from openapi_client.models.trip_resource_relationships_shape_links import TripResourceRelationshipsShapeLinks
from openapi_client.models.trips import Trips
from openapi_client.models.vehicle import Vehicle
from openapi_client.models.vehicle_resource import VehicleResource
from openapi_client.models.vehicle_resource_attributes import VehicleResourceAttributes
from openapi_client.models.vehicle_resource_relationships import VehicleResourceRelationships
from openapi_client.models.vehicles import Vehicles


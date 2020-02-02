# ScheduleResource

A schedule is the arrival drop off (`*/attributes/drop_off_type`) time (`*/attributes/arrival_time`) and departure pick up (`*/attributes/pickup_type`) time (`*/attributes/departure_time`) to/from a stop (`*/relationships/stop/data/id`) at a given sequence (`*/attributes/stop_sequence`) along a trip (`*/relationships/trip/data/id`) going in a direction (`*/attributes/direction_id`) on a route (`*/relationships/route/data/id`) when the trip is following a service (`*/relationships/service/data/id`) to determine when it is active.  See [GTFS `stop_times.txt`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) for base specification. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The JSON-API resource type | [optional] 
**relationships** | [**ScheduleResourceRelationships**](ScheduleResourceRelationships.md) |  | [optional] 
**links** | [**object**](.md) |  | [optional] 
**id** | **str** | The JSON-API resource ID | [optional] 
**attributes** | [**ScheduleResourceAttributes**](ScheduleResourceAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



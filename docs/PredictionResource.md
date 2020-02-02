# PredictionResource

The predicted arrival time (`/*/attributes/arrival_time`) and departure time (`*/attributes/departure_time`) to/from a stop (`*/relationships/stop/data/id`) at a given sequence (`*/attriutes/stop_sequence`) along a trip (`*/relationships/trip/data/id`) going a direction (`*/attributes/direction_id`) along a route (`*/relationships/route/data/id`).  See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `TripDescriptor`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-tripdescriptor) See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `StopTimeUpdate`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-stoptimeupdate) 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The JSON-API resource type | [optional] 
**relationships** | [**PredictionResourceRelationships**](PredictionResourceRelationships.md) |  | [optional] 
**links** | [**object**](.md) |  | [optional] 
**id** | **str** | The JSON-API resource ID | [optional] 
**attributes** | [**PredictionResourceAttributes**](PredictionResourceAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



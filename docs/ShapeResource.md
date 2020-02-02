# ShapeResource

Shape representing the stops to which a particular trip can go. Trips grouped under the same route can have different shapes, and thus different stops. See [GTFS `shapes.txt`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#shapestxt) 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The JSON-API resource type | [optional] 
**relationships** | [**ShapeResourceRelationships**](ShapeResourceRelationships.md) |  | [optional] 
**links** | [**object**](.md) |  | [optional] 
**id** | **str** | The JSON-API resource ID | [optional] 
**attributes** | [**ShapeResourceAttributes**](ShapeResourceAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



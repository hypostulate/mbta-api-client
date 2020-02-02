# ServiceResourceAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_days** | **list[float]** |  | [optional] 
**start_date** | **date** | Earliest date which is valid for this service. Format is ISO8601. | [optional] 
**schedule_typicality** | **int** | Describes how well this schedule represents typical service for the listed &#x60;schedule_type&#x60;  | Value | Description                                                                 | |-------|-----------------------------------------------------------------------------| | &#x60;0&#x60;   | Not defined.                                                                | | &#x60;1&#x60;   | Typical service with perhaps minor modifications                            | | &#x60;2&#x60;   | Extra service supplements typical schedules                                 | | &#x60;3&#x60;   | Reduced holiday service is provided by typical Saturday or Sunday schedule  | | &#x60;4&#x60;   | Major changes in service due to a planned disruption, such as construction  | | &#x60;5&#x60;   | Major reductions in service for weather events or other atypical situations |  | [optional] 
**schedule_type** | **str** | Description of the schedule type the service_id can be applied. For example, on a holiday, the schedule_type value may be \&quot;Saturday\&quot; or \&quot;Sunday\&quot;. Current valid values are \&quot;Weekday\&quot;, \&quot;Saturday\&quot;, \&quot;Sunday\&quot;, or \&quot;Other\&quot;  | [optional] 
**schedule_name** | **str** | Description of when the &#x60;service_id&#x60; is in effect. | [optional] 
**removed_dates_notes** | **list[str]** |  | [optional] 
**removed_dates** | **list[date]** |  | [optional] 
**rating_start_date** | **date** | Earliest date which is a part of the rating (season) which contains this service. Format is ISO8601. | [optional] 
**rating_end_date** | **date** | Latest date which is a part of the rating (season) which contains this service. Format is ISO8601. | [optional] 
**rating_description** | **str** | Human-readable description of the rating (season), as it should appear on public-facing websites and applications. | [optional] 
**end_date** | **date** | Latest date which is valid for this service. Format is ISO8601. | [optional] 
**description** | **str** | Human-readable description of the service, as it should appear on public-facing websites and applications. | [optional] 
**added_dates_notes** | **list[str]** |  | [optional] 
**added_dates** | **list[date]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



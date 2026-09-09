SELECT
	event_category,
    point_name,
    point_value,
    description,
    actor,
    FORMAT(event_timestamp, 'yyyy-MM-dd HH:mm:ss') AS event_timestamp
FROM soe_AR 
ORDER BY event_timestamp DESC
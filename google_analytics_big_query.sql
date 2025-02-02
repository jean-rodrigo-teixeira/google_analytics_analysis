SELECT
  visitorId,
  visitNumber,
  visitStartTime,
  geoNetwork.country,
  geoNetwork.city,
  trafficSource.source,
  trafficSource.medium,
  device.deviceCategory,
  totals.transactionRevenue,
  totals.pageviews,
  totals.timeOnSite,
  CASE 
    WHEN device.deviceCategory = 'mobile' THEN 'A'
    WHEN device.deviceCategory = 'desktop' THEN 'B'
    ELSE 'Others'
  END AS test_device_type
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20170101' AND '20170131'
ORDER BY
  visitStartTime
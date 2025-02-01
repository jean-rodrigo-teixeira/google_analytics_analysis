SELECT
  visitorId,
  visitNumber,
  visitStartTime,
  geoNetwork.country,
  geoNetwork.city,
  trafficSource.source,
  trafficSource.medium,
  totals.transactionRevenue,
  totals.pageviews,
  totals.timeOnSite,
  CASE 
    WHEN trafficSource.medium = 'organic' THEN 'A'
    WHEN trafficSource.medium IN ('cpc', 'paid') THEN 'B'
    ELSE 'Others'
  END AS test_A_B
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20170101' AND '20170131'
ORDER BY
  visitStartTime

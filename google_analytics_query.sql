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
    WHEN trafficSource.medium = 'organic' THEN 'Grupo A'
    WHEN trafficSource.medium IN ('cpc', 'paid') THEN 'Grupo B'
    ELSE 'Outros'
  END AS grupo
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20170101' AND '20170131'
ORDER BY
  visitStartTime

SELECT L.FLAVOR
FROM(
    SELECT 
    (
        SELECT ST
        FROM
        (
            SELECT SUM(TOTAL_ORDER) AS ST, FLAVOR
            FROM JULY
            WHERE 1=1
            GROUP BY FLAVOR
        ) AS J
        WHERE J.FLAVOR = FH.FLAVOR)
        +
    (
        SELECT ST
        FROM
        (
            SELECT SUM(TOTAL_ORDER) AS ST, FLAVOR
            FROM FIRST_HALF
            WHERE 1=1
            GROUP BY FLAVOR
        ) AS F
        WHERE F.FLAVOR = FH.FLAVOR
    ) AS T,
    FH.FLAVOR
    FROM FIRST_HALF AS FH
    ORDER BY T DESC
    LIMIT 3
) AS L;
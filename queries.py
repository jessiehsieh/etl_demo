
# Create a table
DROP_TABLE_QUERY = '''
    DROP TABLE if exists {table_name}
'''

CREATE_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        birthday TEXT NOT NULL,
        gender TEXT NOT NULL,
        website TEXT NOT NULL,
        image TEXT NOT NULL,
        street TEXT NOT NULL,
        streetName TEXT NOT NULL,
        buildingNumber TEXT NOT NULL,
        city TEXT NOT NULL,
        zipcode TEXT NOT NULL,
        country TEXT NOT NULL,
        county_code TEXT NOT NULL,
        latitude TEXT NOT NULL,
        longitude TEXT NOT NULL,
        age TEXT NOT NULL,
        age_group TEXT NOT NULL,
        email_domain TEXT NOT NULL
        )
'''

QUERY_PERCENTAGE_DE_USERS_WITH_GMAIL= """
    SELECT
        printf("%.2f", SUM(CASE WHEN email_domain like '%gmail%'
                        AND country = 'Germany'
                        THEN 1
                ELSE 0 END) *100)/ COUNT(*) AS percentage
    FROM
        persons
"""

QUERY_TOP_3_COUNTRIES_WITH_GMAIL="""
    WITH gmail_country AS 
        (SELECT
            country, count(*) as num_records, RANK() over (ORDER BY count(*) DESC) AS num_records_rank
        FROM
            persons
        WHERE
            (email_domain like '%gmail%')
        GROUP BY country
        ORDER BY num_records desc)
    SELECT country, num_records, num_records_rank
    FROM gmail_country
    WHERE num_records_rank<=3
"""

QUERY_OVER_60YO_WITH_GMAIL="""
    WITH split(age_older_than, age_equal_less) AS (
        SELECT 
            CAST(SUBSTR(age_group, INSTR(age_group, '(') + 1, INSTR(age_group, ',') - 2) AS INTEGER) AS age_older_than,
            CAST(RTRIM(SUBSTR(age_group, INSTR(age_group, ',') + 1), ']') AS INTEGER) AS age_equal_less
        FROM persons
        WHERE
            (email_domain like '%gmail%')
        )
    SELECT count(*) FROM split
    WHERE age_older_than > 60
    ;
"""

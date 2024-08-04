-- Use the specified database
USE your_database_name;

-- Query the information_schema to get the table description
SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Column Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_DEFAULT AS 'Default Value',
    EXTRA AS 'Extra Information'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'Books';

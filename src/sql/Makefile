all:
	make drop_all
	make create_database
	make create_table
	make insert_random_data
	make convert_timestamp

mock:
	make drop_all
	make create_database
	make create_table
	make insert_mock_data
	make convert_timestamp

create_database:
	mysql < big_data_indexing_database_create.sql

create_table:
	mysql big_data_indexing < user_information_table_create.sql

insert_random_data:
	mysql big_data_indexing < user_information_random_data_insert.sql

insert_mock_data:
	mysql big_data_indexing < user_information_mock_data_insert.sql

convert_timestamp:
	mysql big_data_indexing < user_information_convert_time.sql

drop_all:
	-mysql < big_data_indexing_database_drop.sql

mysql:
	mysql big_data_indexing
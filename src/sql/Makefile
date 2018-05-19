all:
	make drop_all
	make create_database
	make create_table
	make insert_data
	make convert_timestamp

create_database:
	mysql -u root < big_data_indexing_database_create.sql

create_table:
	mysql -u root big_data_indexing < user_information_table_create.sql

insert_data:
	mysql -u root big_data_indexing < user_information_data_insert.sql

convert_timestamp:
	mysql -u root big_data_indexing < user_information_convert_time.sql

drop_all:
	mysql -u root -e 'drop database big_data_indexing;'
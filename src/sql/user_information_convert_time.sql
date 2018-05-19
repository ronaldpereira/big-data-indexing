alter table user_information add column create_time_placeholder int(8);
alter table user_information add column update_time_placeholder int(8);
update user_information set create_time_placeholder = UNIX_TIMESTAMP(create_time) where create_time is not null;
update user_information set update_time_placeholder = UNIX_TIMESTAMP(update_time) where update_time is not null;
alter table user_information drop column create_time;
alter table user_information drop column update_time;
alter table user_information change column create_time_placeholder create_time int(8);
alter table user_information change column update_time_placeholder update_time int(8);


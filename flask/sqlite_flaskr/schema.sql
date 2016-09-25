drop table if exists entries;
create table entries(
    id INTEGER primary key autoincrement,
    title text not null,
    content text not null
);

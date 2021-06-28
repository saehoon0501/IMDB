
#Strong Entity 생성
create table Movie(
	title_id varchar(20),
    title_type varchar(20),
    primary_title varchar(2048),
    original_title varchar(2048),
    is_adult boolean,
    start_year int,
    end_year int,
    runtime_minutes int,
    primary key(title_id));
    
create table Person(
	name_id varchar(20),
    deathYear int,
    birthYear int,
    primary_name varchar(200),
    primary key (name_id)
    );
    
create table Review(
	tconst varchar(20),
    average_rating float,
    num_votes int,
    primary key (tconst));
    

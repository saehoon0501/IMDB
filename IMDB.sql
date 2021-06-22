#영화제목을 입력 -> 매칭되는 영화 검색
select *
from Movie
where primaryTitle = 'Reservoir Dogs';

#특정 배우가 등장하는 영화를 별점이 높은 순으로 검색
#먼저 해당 배우 name_id를 얻음
select *
from Person
where primaryName = 'Brad pitt';

#얻은 name_id를 이용해 Role Table의 외래키 name_id로 해당 배우가 배우로 출연한 작품 검색 nested subQuery
select *
from Role r
where r.category= 'actor' and r.name_id in (select name_id
from Person
where primaryName = 'Brad pitt');

#double nested subQuery와 Review Table과 Movie Table의 join을 통해 해당 배우가 출연한 영화를 별점이 높은 순으로 검색한다
select *
from Movie m,Review r
where r.tconst = m.title_id and m.title_id in ( select title_id from Role r where r.category='actor' and r.name_id in (select name_id from Person where primaryName = 'Brad pitt'))
order by averageRating desc;

#특정 감독이 제작한 영화를 개봉연도순으로 검색
select name_id
from Person
where primaryName = 'Quentin Tarantino';

#Directors Table을 사용해 nested Query로 해당 감독이 참여한 영화 title_id 찾음
select distinct title_id
from Directors
where name_id = (select name_id	from Person	where primaryName = 'Quentin Tarantino');

#찾은 title_id를 Movie Table과 join한 후 이를 개봉연도순으로 검색
select *
from Movie m
where titleType = 'movie' and m.title_id in (select distinct title_id	from Directors	where name_id = (select name_id	from Person	where primaryName = 'Quentin Tarantino'))
order by startYear asc;

#Drama 장르의 영화를 리뷰가 많은 순 또는 별점이 높은순으로 검색
#Genre Table에서 drama에 해당하는 record만 가져온다.
select *
from Genre
where genres ='drama';

#Genre에서 drama에 해당하는 title_id와 Movie title_id inner join
select m.*, g.genres
from Movie m
inner join Genre g on m.title_id = g.title_id
where g.genres = 'drama';

#Review Table과 join하여 별점이 높은순으로 검색 및 나열
select k.*,r.averageRating,r.numVotes
from (select m.*,g.genres from Movie m inner join Genre g on m.title_id = g.title_id where g.genres = 'drama') k
inner join Review r on r.tconst = title_id
order by averageRating desc;

#검색한 배우 Brad pitt와 감독 Quentin Tarantino가 같이한 작품을 찾아본다.

#영화배우 Brad pitt가 출연한 작품들 검색
select *
from Movie m
where m.title_id in ( select title_id from Role r where r.category='actor' and r.name_id in (select name_id from Person where primaryName = 'Brad pitt'));

#감독 Quentin Tarantino가 연출한 작품들 검색
select *
from Movie m
where m.title_id in ( select title_id from Role r where r.category='director' and r.name_id in (select name_id from Person where primaryName = 'Quentin Tarantino'));

#위 둘 결과를 title_id로 join하여 같이한 작품 검색한다.
select a.*
from (select *	from Movie m where m.title_id in ( select title_id from Role r where r.category='actor' and r.name_id in (select name_id from Person where primaryName = 'Brad pitt'))) a,
(select * from Movie m where m.title_id in ( select title_id from Role r where r.category='director' and r.name_id in (select name_id from Person where primaryName = 'Quentin Tarantino'))) b
where a.title_id = b.title_id
group by a.title_id;

select g.genres, count(m.title_id)
from Movie m, (select distinct * from Genre) g
where m.title_id = g.title_id
group by g.genres;

Create index Name_index on Person(primaryName);
Create index Title_index on Movie(primaryTitle);

Create index Genre_index on Genre(genres);

ALTER TABLE Genre DROP INDEX Genre_index;

Create index Movie_index on Movie(startYear);

ALTER TABLE Movie DROP INDEX Movie_index;












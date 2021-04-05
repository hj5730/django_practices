desc emaillist;

-- insert
insert into emaillist values(null, '김', '현지', 'hj5730@naver.com');
insert into emaillist values(null, '둘', '리', 'dooly@naver.com');

-- select
select no, first_name, last_name, email
from emaillist
order by no desc;

select * from emaillist;

-- schema
desc guestbook;

-- insert
insert into guestbook values(null, '김현지', '1234', 'Hi!', now());

-- select
  select no,
         name,
         message,
         date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date
    from guestbook
order by reg_date desc;

-- delete
delete
  from guestbook
 where no = 1
   and password = '1234';

SELECT * FROM users WHERE birth_year<=1990 AND fname='Maria';

select * from users where sname LIKE 'petrov%';

-- show all orders for users born in 1990
select *
	from test.users as users, test.orders as orders
	where users.birth_year=1990 AND users.order_id=orders.id;


-- HW: delete all orders for users born in 1990
delete from test.users as users, test.orders as orders
	where users.birth_year=1990 AND users.order_id=orders.id;
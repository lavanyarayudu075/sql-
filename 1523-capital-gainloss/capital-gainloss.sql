# Write your MySQL query statement below
select distinct(stock_name),
sum(case
when operation = 'sell' then price
when operation = 'buy' then -price
end) as capital_gain_loss
from stocks
group by stock_name
order by capital_gain_loss desc;
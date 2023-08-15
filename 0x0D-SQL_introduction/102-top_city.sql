-- displays top 3 city temperatures during july and august ordered by temp
SELECT city, AVG(value) as 'avg_temp' FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY `avg_temp` DESC LIMIT 3;

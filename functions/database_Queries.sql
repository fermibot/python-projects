SELECT
	bookName                        Book,
	firstName || ' ' || lastName AS Author,
	series                          BookSeries
FROM books
	LEFT OUTER JOIN authorBook a ON books.bookID = a.bookFK
	LEFT OUTER JOIN authors ON authorFK = authorID
WHERE Author IS NOT NULL
			AND bookname LIKE '%opt%'
ORDER BY BookSeries, Book, Author;

-- SELECT
-- 	coin.denominationName,
-- 	n.denominationSeries,
-- 		geography.geoLocation,
-- 	denominationYear,
-- 	denominationHave
-- FROM numismatics_master coin
-- 	LEFT OUTER JOIN geography ON geography.geoCode = coin.denominationGeoCode
-- 	LEFT OUTER JOIN numismatics_series n ON coin.denominationSeriesId = n.denominationSeriesId
-- WHERE denominationHave = 0
-- ORDER BY n.denominationSeries, denominationName;


-- DELETE FROM authors
-- WHERE authorID > 61;
--
-- DELETE FROM books
-- WHERE bookid > 62;
--
-- DELETE FROM authorBook WHERE ID > 68;

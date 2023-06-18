-- SQL script that lists all bands with `Glam rock` as
-- their main style, ranked by their longevity.
SELECT band_name, IFNULL((split - formed), YEAR(CURDATE()) - formed) AS longevity
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY longevity DESC;

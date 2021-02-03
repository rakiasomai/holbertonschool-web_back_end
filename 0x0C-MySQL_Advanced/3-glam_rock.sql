-- table user creation
SELECT band_name, COALESCE(split, 2020) - formed as lifespan FROM metal_bands WHERE style like '%Glam rock%' ORDER BY lifespan DESC;;
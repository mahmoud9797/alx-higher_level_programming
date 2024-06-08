-- delete george and add Aria
DELETE FROM second_table WHERE name = "George";
INSERT INTO second_table (`id`, name, `score`) VALUES (5, "Aria", 12), (6, "Aria", 18);

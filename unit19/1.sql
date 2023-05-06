SELECT teachers.full_name
FROM teachers
         JOIN assignments USING(teacher_id)
         JOIN assignments_grades USING (assisgnment_id)
GROUP BY teachers.full_name
ORDER BY avg(assignments_grades.grade)
LIMIT 1
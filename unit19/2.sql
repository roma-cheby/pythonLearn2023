SELECT students.full_name
FROM students
         JOIN assignments_grades USING (student_id)
GROUP BY students.full_name
ORDER BY avg(assignments_grades.grade) DESC
LIMIT 10
SELECT students.full_name
FROM students
         JOIN students_groups USING (group_id)
         JOIN teachers USING (teacher_id)
WHERE teachers.full_name =
      (SELECT teachers.full_name
       FROM teachers
                JOIN assignments USING(teacher_id)
                JOIN assignments_grades USING (assisgnment_id)
       GROUP BY teachers.full_name
       ORDER BY avg(assignments_grades.grade) DESC
       LIMIT 1)
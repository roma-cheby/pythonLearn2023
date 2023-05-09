SELECT students_groups.group_id, SUM(assignments.due_date < assignments_grades.date)
FROM students_groups
         JOIN assignments USING (group_id)
         JOIN assignments_grades USING (assisgnment_id)
GROUP BY students_groups.group_id

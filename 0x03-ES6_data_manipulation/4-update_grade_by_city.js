export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city)
    .map((student) => {
      for (const field of newGrades) {
        if (students.id === field.id) {
          students.grade = newGrades.grade;
        } else {
          students.grade = 'N/A';
        }
      }
    }
  );
}

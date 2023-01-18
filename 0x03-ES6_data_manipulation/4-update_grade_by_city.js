export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city)
    .map((student) => {
      for (const field of newGrades) {
        if (student.id === field.id) {
          student.grade = newGrades.grade;
        } else {
          student.grade = 'N/A';
        }
      }
    }
  );
}

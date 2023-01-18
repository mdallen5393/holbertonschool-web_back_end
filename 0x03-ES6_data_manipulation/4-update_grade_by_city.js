export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city)
    .map((student) => {
      student.grade = 'N/A';
      for (const field of newGrades) {
        if (student.id === field.id) {
          student.grade = newGrades.grade;
        }
      }
    }
  );
}

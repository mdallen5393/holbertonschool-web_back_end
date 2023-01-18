export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) =>
    student.location === city).map((student) => {
      if (students.id === newGrades.id) {
        students.grade = newGrades.grade;
      } else {
        students.grade = 'N/A';
      }
    });

}

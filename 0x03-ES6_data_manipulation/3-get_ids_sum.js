export default function getStudentIdsSum(students) {
  let sum = 0;
  return students.reduce((sum, curr) => sum + students.id);
}
export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const students_map = new Map(students);
  return [...students_map.get('id')];
}
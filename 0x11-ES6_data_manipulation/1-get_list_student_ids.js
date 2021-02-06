export default function getListStudentIds(student) {
    if (Array.isArray(student) == false) {
    return [];
    }
    return student.map((l_student) => (l_student.id));
}
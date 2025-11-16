document.addEventListener('DOMContentLoaded', async function() {
    const students = await getStudents();
    document.getElementById('total-students').textContent = students.length;
});
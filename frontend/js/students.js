document.addEventListener('DOMContentLoaded', async function() {
    const students = await getStudents();
    const studentsTableBody = document.querySelector('#students-table tbody');

    students.forEach(student => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.rollNo}</td>
            <td>${student.class}</td>
            <td>${student.email}</td>
            <td class="actions">
                <a href="student-details.html?id=${student.id}">View</a>
                <a href="#" class="edit-btn">Edit</a>
                <a href="#" class="delete-btn">Delete</a>
            </td>
        `;
        studentsTableBody.appendChild(row);
    });
});
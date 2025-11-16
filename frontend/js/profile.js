document.addEventListener('DOMContentLoaded', async function() {
    const urlParams = new URLSearchParams(window.location.search);
    const studentId = parseInt(urlParams.get('id'));

    if (studentId) {
        const student = await getStudentById(studentId);
        const profileContainer = document.getElementById('profile-container');
        if (student) {
            profileContainer.innerHTML = `
                <div><strong>Name:</strong> ${student.name}</div>
                <div><strong>Roll No:</strong> ${student.rollNo}</div>
                <div><strong>Class:</strong> ${student.class}</div>
                <div><strong>Email:</strong> ${student.email}</div>
            `;
        } else {
            profileContainer.innerHTML = '<p>Student not found.</p>';
        }
    }
});
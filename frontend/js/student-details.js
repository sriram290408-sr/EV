document.addEventListener("DOMContentLoaded", () => {
    const studentId = new URLSearchParams(window.location.search).get('id');
    const student = students.find(s => s.id === parseInt(studentId));

    const container = document.getElementById('student-details-container');

    if (student) {
        container.innerHTML = `
            <div class="student-details-grid">
                <div class="student-photo">
                    <img src="../img/student-placeholder.png" alt="Student Photo">
                </div>
                <div class="student-info">
                    <p><strong>Name:</strong> ${student.name}</p>
                    <p><strong>Roll No:</strong> ${student.rollNo}</p>
                    <p><strong>Class:</strong> ${student.class}</p>
                    <p><strong>Email:</strong> ${student.email}</p>
                    <p><strong>Address:</strong> ${student.address || 'N/A'}</p>
                    <p><strong>Contact:</strong> ${student.contact || 'N/A'}</p>
                </div>
            </div>
        `;
    } else {
        container.innerHTML = '<p>Student not found.</p>';
    }
});
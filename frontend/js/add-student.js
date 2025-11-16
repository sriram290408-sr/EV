document.addEventListener('DOMContentLoaded', function() {
    const addStudentForm = document.getElementById('add-student-form');

    addStudentForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const newStudent = {
            id: students.length + 1, // This is a simple way to generate a new ID
            name: document.getElementById('name').value,
            rollNo: document.getElementById('rollNo').value,
            class: document.getElementById('class').value,
            email: document.getElementById('email').value,
            dob: document.getElementById('dob').value,
            contact: document.getElementById('contact').value,
        };

        students.push(newStudent);

        // In a real application, you would send this data to a server.
        // For this example, we'll just show an alert.
        alert('Student added successfully!');
        window.location.href = 'students.html';
    });
});
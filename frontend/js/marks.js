// js/marks.js
document.addEventListener('DOMContentLoaded', () => {

    const studentSelect = document.getElementById('student-select');
    const marksForm = document.getElementById('marks-form');

    function populateStudentDropdown() {
        const students = getStudents();
        if (students.length > 0) {
            studentSelect.innerHTML = '<option value="">Select a student</option>';
            students.forEach(student => {
                const option = document.createElement('option');
                option.value = student.rollNo;
                option.textContent = `${student.name} (${student.rollNo})`;
                studentSelect.appendChild(option);
            });
        } else {
            studentSelect.innerHTML = '<option value="">No students available</option>';
        }
    }

    marksForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const rollNo = studentSelect.value;
        const subject = document.getElementById('subject').value;
        const marks = document.getElementById('marks').value;

        if (!rollNo) {
            alert('Please select a student.');
            return;
        }

        const newMark = {
            rollNo, // include rollNo to associate the mark with the student
            subject,
            marks,
            date: new Date().toLocaleDateString()
        };

        addMark(newMark);
        alert('Marks added successfully!');
        marksForm.reset();
    });

    populateStudentDropdown();
});
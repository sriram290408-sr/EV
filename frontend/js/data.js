const students = [
    { id: 1, name: 'John Doe', rollNo: 'A123', class: '10A', email: 'john.doe@example.com' },
    { id: 2, name: 'Jane Smith', rollNo: 'B456', class: '10B', email: 'jane.smith@example.com' },
    { id: 3, name: 'Peter Jones', rollNo: 'C789', class: '11A', email: 'peter.jones@example.com' },
    { id: 4, name: 'Mary Johnson', rollNo: 'D101', class: '11B', email: 'mary.johnson@example.com' },
];

function getStudents() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(students);
        }, 500);
    });
}

function getStudentById(id) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(students.find(s => s.id === id));
        }, 500);
    });
}
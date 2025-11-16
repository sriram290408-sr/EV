document.addEventListener('DOMContentLoaded', () => {
    const studentSelect = document.getElementById('student-select-dashboard');
    const subjectPerformanceCtx = document.getElementById('subjectPerformanceChart')?.getContext('2d');
    const improvementCtx = document.getElementById('improvementChart')?.getContext('2d');

    let subjectPerformanceChart, improvementChart;

    // Function to get data from LocalStorage
    const getStudents = () => JSON.parse(localStorage.getItem('students')) || [];
    const getMarks = () => JSON.parse(localStorage.getItem('marks')) || {};

    // Populate student dropdown
    const populateStudentDropdown = () => {
        const students = getStudents();
        if (studentSelect) {
            students.forEach(student => {
                const option = document.createElement('option');
                option.value = student.rollNo;
                option.textContent = `${student.name} (${student.rollNo})`;
                studentSelect.appendChild(option);
            });
        }
    };

    // Update charts for a selected student
    const updateCharts = (rollNo) => {
        const allMarks = getMarks();
        const studentMarks = allMarks[rollNo] || [];

        // Destroy existing charts if they exist
        if (subjectPerformanceChart) subjectPerformanceChart.destroy();
        if (improvementChart) improvementChart.destroy();

        if (!studentMarks.length) return;

        // 1. Subject Performance Chart (Bar Chart)
        const subjects = {};
        studentMarks.forEach(mark => {
            if (!subjects[mark.subject]) {
                subjects[mark.subject] = [];
            }
            subjects[mark.subject].push(parseFloat(mark.marks));
        });

        const subjectLabels = Object.keys(subjects);
        const subjectAverages = subjectLabels.map(subject => {
            const marks = subjects[subject];
            const average = marks.reduce((a, b) => a + b, 0) / marks.length;
            return average;
        });

        if (subjectPerformanceCtx) {
            subjectPerformanceChart = new Chart(subjectPerformanceCtx, {
                type: 'bar',
                data: {
                    labels: subjectLabels,
                    datasets: [{
                        label: 'Average Marks per Subject',
                        data: subjectAverages,
                        backgroundColor: 'rgba(15, 76, 129, 0.6)',
                        borderColor: 'rgba(15, 76, 129, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            });
        }

        // 2. Improvement Chart (Line Chart)
        const terms = {};
        studentMarks.forEach(mark => {
            if (!terms[mark.term]) {
                terms[mark.term] = [];
            }
            terms[mark.term].push(parseFloat(mark.marks));
        });

        const termLabels = Object.keys(terms).sort(); // Sort terms chronologically
        const termAverages = termLabels.map(term => {
            const marks = terms[term];
            const average = marks.reduce((a, b) => a + b, 0) / marks.length;
            return average;
        });

        if (improvementCtx) {
            improvementChart = new Chart(improvementCtx, {
                type: 'line',
                data: {
                    labels: termLabels,
                    datasets: [{
                        label: 'Average Marks Over Terms',
                        data: termAverages,
                        fill: false,
                        borderColor: 'rgba(255, 123, 0, 1)',
                        tension: 0.1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            });
        }
    };

    // Event listener for student selection
    if (studentSelect) {
        studentSelect.addEventListener('change', () => {
            const selectedRollNo = studentSelect.value;
            updateCharts(selectedRollNo);
        });
    }

    // Initial setup
    populateStudentDropdown();
});
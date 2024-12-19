// Get the canvas element
const ctx = document.getElementById('taskStatusChart').getContext('2d');

// Create a new chart instance
const myChart = new Chart(ctx, {
    type: 'bar', // Chart type (e.g., 'bar', 'line', 'pie', etc.)
    data: {
        labels: ['Project 1', 'Project 2', 'Project 3'], // X-axis labels
        datasets: [{
            label: 'Progress (%)',
            data: [70, 45, 90], // Data points
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

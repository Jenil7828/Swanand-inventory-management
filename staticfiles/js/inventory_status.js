document.addEventListener("DOMContentLoaded", function() {
  // Dark Mode Toggle
  const toggleDarkModeButton = document.getElementById("toggleDarkMode");
  const bodyElement = document.body;

  // Dark mode toggle logic with icon change
  toggleDarkModeButton.addEventListener("click", () => {
    bodyElement.classList.toggle("dark-mode");
    const isDarkMode = bodyElement.classList.contains("dark-mode");
    localStorage.setItem("theme", isDarkMode ? "dark" : "light");
    toggleDarkModeButton.textContent = isDarkMode ? "☀️" : "🌙"; // Toggle icon
  });

  // Check if the theme is stored in localStorage and apply it
  if (localStorage.getItem("theme") === "dark") {
    bodyElement.classList.add("dark-mode");
    toggleDarkModeButton.textContent = "☀️"; // Set icon to sun when dark mode is applied
  } else {
    toggleDarkModeButton.textContent = "🌙"; // Set icon to moon when light mode is applied
  }

  // Sidebar Toggle
  const sidebar = document.getElementById("sidebar");

  function toggleSidebar() {
    sidebar.classList.toggle("collapsed");

    const btn = document.querySelector(".toggle-sidebar");
    btn.style.left = sidebar.classList.contains("collapsed") ? '1rem' : '240px';
  }

  // Parse the JSON data passed from Django into JavaScript object
  const stockEl = document.getElementById("stock-data");
  let stockData = [];

  try {
    stockData = JSON.parse(stockEl.textContent);
    console.log("✅ Parsed inventory data:", stockData);
  } catch (err) {
    console.error("❌ Failed to parse inventory JSON:", err.message);
    return;
  }

  // Process stock data into separate location data arrays
  const locations = [...new Set(stockData.map(item => item.location))];
  const locationData = locations.map(location => stockData.filter(item => item.location === location));

  // Color palette for pie charts
  const chartColors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c2c2f0', '#ffb3e6'];

  // Loop through each location and create a pie chart for it
  locations.forEach((location, index) => {
    const data = locationData[index];
    const productLabels = data.map(item => item.product);
    const quantities = data.map(item => item.quantity);

    // Create a new canvas element for the chart
    const canvas = document.createElement('canvas');
    document.getElementById('charts-container').appendChild(canvas);

    // Generate the pie chart using Chart.js
    new Chart(canvas, {
      type: 'pie',  // Pie chart type
      data: {
        labels: productLabels,
        datasets: [{
          label: `Stock Quantity at ${location}`,
          data: quantities,
          backgroundColor: chartColors.slice(0, data.length), // Assign different colors dynamically
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            labels: {
              font: {
                size: 30  // Font size for legend
              }
            }
          },
          title: {
            display: true,
            text: `Inventory Distribution for ${location}`,
            font: {
              size: 38,
              weight: 'bold',
              family: 'Arial'
            }
          },
          tooltip: {
            titleFont: {
              size: 30,  // Title font size for tooltips
              weight: 'bold'
            },
            bodyFont: {
              size: 20,  // Body font size for tooltips
            },
            padding: 10,  // Padding inside the tooltip
            boxPadding: 10  // Padding around the tooltip box
          },
          datalabels: {
            color: '#fff',
            font: {
              weight: 'bold',
              size: 72  // Font size for data labels
            },
            formatter: (value) => value  // Display the quantity value in the label
          }
        }
      },
      plugins: [ChartDataLabels]  // Use the ChartDataLabels plugin for data labels
    });
  });
});
